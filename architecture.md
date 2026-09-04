# Architecture — BolKeHisab

## Goals

1. Turn unstructured multimodal input into a trustworthy financial ledger.
2. Keep the merchant in control at every money-adjacent step.
3. Prefer refusal and confirmation over hallucination.
4. Make every number explainable (provenance).

## Components

### 1. Multimodal Intake
- Voice notes, photos of notebooks, UPI screenshots, text messages
- Normalized into IngestEvent objects

### 2. Perception Layer (AI)
- Speech-to-Text (Hinglish-aware)
- Vision / OCR for handwritten pages
- Transaction extraction with confidence scores
- Never writes directly to the ledger

### 3. Living Ledger Engine (Deterministic)
- Double-entry style reconstruction
- Full provenance for every entry
- Confidence scoring + human confirmation gates

### 4. Agentic Layer (Bounded)
- Natural language Q&A grounded in the ledger
- Action proposals only (payment links, messages, alerts)
- Hard Policy Engine sits above the LLM

## Trust Guardrails

| Risk                     | Mitigation                                   |
|--------------------------|----------------------------------------------|
| Hallucinated balances    | Ledger is source of truth                    |
| Silent money movement    | Zero auto-execution, explicit confirm needed |
| Bad OCR / STT            | Confidence gates + human confirmation        |
| Conflicting inputs       | Deterministic conflict detection             |

## Why This Satisfies the Open Track Bar

- **Real problem**: Financial invisibility of informal merchants
- **Working product**: End-to-end ingest → ledger → Q&A → gated actions
- **Meaningful AI**: Multimodal perception + constrained agent
- **Evidence of value**: Accuracy metrics + exception list
- **Reliability**: Deterministic core + policy engine + provenance
