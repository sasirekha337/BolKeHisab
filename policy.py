"""
Hard policy engine that sits above the LLM.
Never allows unsupervised money movement or invented balances.
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel


class ActionType(str, Enum):
    ANSWER_QUESTION = "answer_question"
    GENERATE_PAYMENT_LINK = "generate_payment_link"
    DRAFT_MESSAGE = "draft_message"
    FLAG_SHORTFALL = "flag_shortfall"
    REQUEST_CONFIRMATION = "request_confirmation"
    REFUSE = "refuse"


class PolicyDecision(BaseModel):
    allowed: bool
    action: ActionType
    reason: str
    requires_human_confirm: bool = True
    confidence_threshold: float = 0.75


def evaluate_action(
    action: ActionType,
    confidence: float,
    involves_money_movement: bool = False,
    ledger_is_confirmed: bool = False,
) -> PolicyDecision:
    """
    Deterministic policy. The LLM may propose; this decides.
    """
    if involves_money_movement:
        return PolicyDecision(
            allowed=False,
            action=ActionType.REFUSE,
            reason="Money movement is never auto-executed. Explicit human confirmation required.",
            requires_human_confirm=True,
        )

    if action == ActionType.GENERATE_PAYMENT_LINK:
        if not ledger_is_confirmed or confidence < 0.8:
            return PolicyDecision(
                allowed=True,
                action=ActionType.REQUEST_CONFIRMATION,
                reason="Payment link generation requires confirmed ledger state and high confidence.",
                requires_human_confirm=True,
            )
        return PolicyDecision(
            allowed=True,
            action=ActionType.GENERATE_PAYMENT_LINK,
            reason="High confidence + confirmed ledger. Link will be generated after final confirm.",
            requires_human_confirm=True,  # still gated
        )

    if confidence < 0.6:
        return PolicyDecision(
            allowed=True,
            action=ActionType.REQUEST_CONFIRMATION,
            reason=f"Confidence {confidence:.2f} below threshold. Asking merchant to confirm.",
            requires_human_confirm=True,
        )

    return PolicyDecision(
        allowed=True,
        action=action,
        reason="Within policy bounds.",
        requires_human_confirm=action in {
            ActionType.GENERATE_PAYMENT_LINK,
            ActionType.DRAFT_MESSAGE,
        },
    )
