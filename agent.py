from fastapi import APIRouter
from pydantic import BaseModel
from policy import evaluate_action, ActionType

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str
    merchant_id: str = "demo-merchant"


class ActionRequest(BaseModel):
    intent: str
    merchant_id: str = "demo-merchant"


@router.post("/ask")
def ask_question(req: QuestionRequest):
    q = req.question.lower()

    if "kitna" in q or "cash" in q or "balance" in q:
        return {
            "answer": "Aaj ka estimated cash position ≈ ₹12,450 hai. Isme ₹3,200 pending in aur ₹1,800 pending out hai.",
            "confidence": 0.82,
            "sources": ["ledger_entries:confirmed", "pending:3"],
            "requires_confirmation": False,
            "policy": evaluate_action(ActionType.ANSWER_QUESTION, confidence=0.82).model_dump(),
        }

    if "pending" in q or "customer" in q:
        return {
            "answer": "Ramesh bhai ka ₹2,400 pending hai (3 din se). Sunita ji ka ₹800 pending hai.",
            "confidence": 0.78,
            "sources": ["entry:ramesh", "entry:sunita"],
            "requires_confirmation": False,
            "policy": evaluate_action(ActionType.ANSWER_QUESTION, confidence=0.78).model_dump(),
        }

    return {
        "answer": "Mujhe is sawal ka clear jawab ledger se nahi mil raha. Kya aap thoda aur detail de sakte hain?",
        "confidence": 0.35,
        "sources": [],
        "requires_confirmation": True,
        "policy": evaluate_action(ActionType.REQUEST_CONFIRMATION, confidence=0.35).model_dump(),
    }


@router.post("/propose")
def propose_action(req: ActionRequest):
    decision = evaluate_action(
        action=ActionType.GENERATE_PAYMENT_LINK,
        confidence=0.85,
        involves_money_movement=False,
        ledger_is_confirmed=True,
    )
    return {
        "proposal": {
            "type": "generate_payment_link",
            "amount": 2400,
            "party": "Ramesh bhai",
            "message_draft": "Ramesh bhai, namaste. Aapka ₹2,400 pending hai. Is link se payment kar dijiye: [Razorpay Link]",
        },
        "policy_decision": decision.model_dump(),
        "next_step": "Human must explicitly confirm before link is generated.",
    }
