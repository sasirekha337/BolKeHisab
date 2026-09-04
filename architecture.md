# Architecture — BolKeHisab

## High-Level Goals

1. Turn unstructured multimodal input into a trustworthy financial ledger.
2. Keep the merchant in control at every money-adjacent step.
3. Prefer refusal and confirmation over hallucination.
4. Make every number explainable (provenance).

## Component Breakdown

### 1. Multimodal Intake Layer
- Accepts:
  - Audio (voice notes)
  - Images (notebook photos, bills, UPI screenshots)
  - Text (chat messages)
- Normalizes everything into a common `IngestEvent` object with source metadata and timestamp.

### 2. Perception Layer (AI)
- **Speech-to-Text**: Hinglish-aware transcription (primary languages: Hindi + English mix).
- **Vision / OCR**: Handwritten and printed text extraction + layout understanding.
- **Extraction Agent**: Turns raw text/transcript into candidate transactions (amount, party, direction, date, notes).
- Outputs structured candidates + confidence scores. Never writes directly to the ledger.

### 3. Living Ledger Engine (Deterministic Core)
- Double-entry style reconstruction.
- Every `LedgerEntry` carries:
  - Amount, accounts, timestamp
  - Full provenance (which IngestEvent(s) created it)
  - Confidence score
  - Confirmation status (`auto`, `pending_human`, `confirmed`, `rejected`)
- Reconciliation rules and conflict detection live here (deterministic).
- Human confirmation queue for low-confidence or conflicting entries.

### 4. Agentic Layer (Bounded)
- Natural language Q&A grounded strictly in the current ledger state (RAG over ledger + provenance).
- Action proposals only:
  - Generate Razorpay payment link (test mode)
  - Draft collection / reminder message in merchant’s tone
  - Cash shortfall / runway alert
- **Policy Engine** sits above the LLM:
  - Hard rules (never auto-send, never invent balances, never execute without confirm)
  - Stopping conditions
  - Audit logging of every proposal

### 5. Interface
- Chat-first (WhatsApp-style) UI.
- Optional simple “Cash Reality” summary screen.
- Designed for low-literacy and voice-primary users.

## Trust & Safety Guardrails

| Risk                        | Mitigation                                      |
|----------------------------|-------------------------------------------------|
| Hallucinated balances      | Ledger is source of truth; LLM only reads it    |
| Silent money movement      | Zero auto-execution; explicit confirm required  |
| Bad OCR / STT              | Confidence gates + human confirmation queue     |
| Conflicting inputs         | Deterministic conflict detection + escalation   |
| Prompt injection           | Structured extraction + policy engine           |

## Failure Modes We Explicitly Handle

1. Ambiguous amounts or parties in voice notes → pending confirmation
2. Partial or overlapping notebook photos → merge logic + human review
3. Duplicate UPI screenshots → idempotency via content hash + timestamp window
4. LLM uncertainty → system responds with “Mujhe confirm karna padega” + shows source

## Data Flow (Happy Path)

```
Voice Note / Photo / Text
        ↓
IngestEvent created
        ↓
Perception (STT / OCR / Extraction) → CandidateTransaction(s)
        ↓
Ledger Engine validates & scores → LedgerEntry (auto or pending)
        ↓
(If pending) Human confirmation via chat
        ↓
Agent can now answer questions or propose actions against confirmed ledger
```

## Technology Choices (MVP)

- Backend: FastAPI + SQLAlchemy + SQLite/Postgres
- AI: Pluggable providers (local or API) for STT, Vision, LLM
- Frontend: Simple React / vanilla JS chat UI
- Storage: Ledger + full event log for auditability
- Auth: Simple merchant session for demo (expandable)

## Why This Architecture Satisfies the Open Track Bar

- **Real problem**: Financial invisibility of informal merchants
- **Working product**: End-to-end ingest → ledger → Q&A → gated actions
- **Meaningful AI**: Multimodal perception + constrained agent (not “LLM does everything”)
- **Evidence of value**: Reconstruction accuracy, confirmation rates, grounded answer rate, honest exception list
- **Reliability & depth**: Deterministic core, provenance, policy engine, explicit failure handling
