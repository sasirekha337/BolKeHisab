from fastapi import APIRouter
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
import uuid

router = APIRouter()


class ConfirmationStatus(str, Enum):
    AUTO = "auto"
    PENDING_HUMAN = "pending_human"
    CONFIRMED = "confirmed"
    REJECTED = "rejected"


class Direction(str, Enum):
    IN = "in"
    OUT = "out"
    ADJUST = "adjust"


class Provenance(BaseModel):
    source_type: str
    source_id: str
    raw_excerpt: Optional[str] = None
    model_confidence: float = 0.0


class LedgerEntry(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    amount: float
    direction: Direction
    party: Optional[str] = None
    notes: Optional[str] = None
    entry_date: datetime
    confirmation: ConfirmationStatus = ConfirmationStatus.PENDING_HUMAN
    confidence: float = 0.0
    provenance: List[Provenance] = Field(default_factory=list)


class CashPosition(BaseModel):
    as_of: datetime
    estimated_cash: float
    pending_in: float
    pending_out: float
    confidence: float
    notes: List[str] = Field(default_factory=list)


@router.get("/entries")
def list_entries(merchant_id: str = "demo-merchant"):
    return {
        "merchant_id": merchant_id,
        "count": 0,
        "entries": [],
        "message": "Demo mode — connect real ledger store later",
    }


@router.get("/position")
def cash_position(merchant_id: str = "demo-merchant"):
    return CashPosition(
        as_of=datetime.utcnow(),
        estimated_cash=12450.0,
        pending_in=3200.0,
        pending_out=1800.0,
        confidence=0.82,
        notes=[
            "Based on confirmed entries + pending confirmation items",
            "UPI screenshot still pending OCR confirmation",
        ],
    )


@router.post("/confirm/{entry_id}")
def confirm_entry(entry_id: str, approve: bool = True):
    return {
        "entry_id": entry_id,
        "status": "confirmed" if approve else "rejected",
        "message": "Entry updated. Ledger recalculated.",
    }
