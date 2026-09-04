"""
Core ledger models with full provenance.
"""

from datetime import datetime
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, Field
import uuid


class ConfirmationStatus(str, Enum):
    AUTO = "auto"
    PENDING_HUMAN = "pending_human"
    CONFIRMED = "confirmed"
    REJECTED = "rejected"


class Direction(str, Enum):
    IN = "in"       # money received
    OUT = "out"     # money paid
    ADJUST = "adjust"


class Provenance(BaseModel):
    source_type: str                    # voice | photo | text | upi_screenshot
    source_id: str
    raw_excerpt: Optional[str] = None
    extracted_at: datetime = Field(default_factory=datetime.utcnow)
    model_confidence: float = 0.0


class LedgerEntry(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    amount: float
    direction: Direction
    party: Optional[str] = None         # customer / supplier name
    notes: Optional[str] = None
    entry_date: datetime
    created_at: datetime = Field(default_factory=datetime.utcnow)
    confirmation: ConfirmationStatus = ConfirmationStatus.PENDING_HUMAN
    confidence: float = 0.0
    provenance: List[Provenance] = Field(default_factory=list)
    account_hint: Optional[str] = None  # cash / bank / upi etc.


class CashPosition(BaseModel):
    as_of: datetime
    estimated_cash: float
    pending_in: float
    pending_out: float
    confidence: float
    notes: List[str] = Field(default_factory=list)
