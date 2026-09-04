from fastapi import APIRouter
from datetime import datetime
from app.models.ledger import CashPosition, LedgerEntry, Direction, ConfirmationStatus

router = APIRouter()

# In-memory demo store (replace with DB in full implementation)
_DEMO_ENTRIES = []


@router.get("/entries")
def list_entries(merchant_id: str = "demo-merchant"):
    return {
        "merchant_id": merchant_id,
        "count": len(_DEMO_ENTRIES),
        "entries": _DEMO_ENTRIES,
    }


@router.get("/position")
def cash_position(merchant_id: str = "demo-merchant"):
    """
    Returns current estimated cash position with confidence.
    """
    return CashPosition(
        as_of=datetime.utcnow(),
        estimated_cash=12450.0,
        pending_in=3200.0,
        pending_out=1800.0,
        confidence=0.82,
        notes=[
            "Based on 14 confirmed entries + 3 pending confirmation",
            "UPI screenshot from yesterday still pending OCR confirmation",
        ],
    )


@router.post("/confirm/{entry_id}")
def confirm_entry(entry_id: str, approve: bool = True):
    return {
        "entry_id": entry_id,
        "status": "confirmed" if approve else "rejected",
        "message": "Entry updated. Ledger recalculated.",
    }
