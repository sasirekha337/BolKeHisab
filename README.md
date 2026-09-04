# BolKeHisab — Voice-First Living Ledger for India’s Informal Merchants

> **Razorpay AI Buildathon 2026 — Open Track**

**BolKeHisab** turns the chaotic, oral, paper-based financial reality of India’s informal merchants into a reliable, auditable living ledger they can actually talk to — without forcing them to change how they already work.

---

## The Problem

Tens of millions of small Indian businesses (kiranas, tea stalls, workshops, neighbourhood shops) do **not** keep formal books. Their system of record is:

- Memory
- WhatsApp voice notes (Hinglish / Hindi)
- Photos of handwritten notebooks
- Scattered UPI screenshots
- Verbal agreements

As a result they cannot reliably answer:

- “Aaj kitna cash hai?”
- “Kaunsa customer pending hai?”
- “Agle hafte shortfall aayega kya?”

This invisibility blocks collections, credit access, and good decisions. Existing tools fail because they assume literacy, English, and structured data entry.

## What BolKeHisab Does

1. **Multimodal Intake**  
   Accepts voice notes, photos of handwritten diaries, UPI screenshots, and chat text.

2. **Living Ledger**  
   Reconstructs a clean, double-entry style ledger with full provenance for every entry.

3. **Natural Language Interface**  
   Merchants (or their helpers) ask questions in everyday Hinglish and get grounded answers.

4. **Bounded Agent Actions**  
   Proposes high-value next steps (generate Razorpay payment link, draft collection message, flag shortfall) — never executes money movement without explicit human confirmation.

5. **Audit & Trust**  
   Every number is traceable. Low-confidence items are gated. The system prefers saying “I don’t know” over inventing figures.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     Multimodal Intake                       │
│  (Voice • Photo • Text • UPI Screenshot)                    │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              Perception Layer (AI)                          │
│  • Speech-to-Text (Hinglish-aware)                          │
│  • Vision / OCR for handwritten pages                       │
│  • Entity & transaction extraction                          │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              Living Ledger Engine (Deterministic)           │
│  • Double-entry reconstruction                              │
│  • Provenance tracking                                      │
│  • Confidence scoring + human confirmation gates            │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              Agentic Layer (Bounded)                        │
│  • Natural language Q&A (grounded in ledger)                │
│  • Action proposals only (payment links, messages, alerts)  │
│  • Hard policy engine above the LLM                         │
└─────────────────────────────────────────────────────────────┘
```

See [`docs/architecture.md`](docs/architecture.md) for detailed design decisions, failure modes, and guardrails.

## Key Design Principles

- **AI is a tool, not the source of truth** — deterministic ledger + policy engine sit above the models.
- **Provenance over perfection** — every entry must explain where it came from.
- **Human-in-the-loop by default** for any low-confidence or money-adjacent action.
- **Culturally native interface** — voice + photo first, not dashboard first.
- **Honest metrics** — we publish reconstruction accuracy, exception rates, and failure cases.

## Project Structure

```
BolKeHisab/
├── backend/                 # FastAPI + core logic
│   ├── app/
│   │   ├── agents/          # Bounded agent logic
│   │   ├── api/             # REST + webhook endpoints
│   │   ├── core/            # Config, security, policy engine
│   │   ├── models/          # Ledger, Transaction, Provenance
│   │   ├── services/        # STT, Vision, Extraction, Ledger
│   │   └── utils/
│   └── tests/
├── frontend/                # Simple chat-style UI (WhatsApp-like)
├── data/
│   ├── samples/             # Real-ish example inputs
│   └── synthetic/           # Controlled test sets for metrics
├── docs/                    # Architecture, decisions, metrics
├── scripts/                 # Setup, evaluation, demo helpers
└── README.md
```

## Quick Start (Development)

```bash
# Clone
git clone <your-repo-url>
cd BolKeHisab

# Backend
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend (separate terminal)
cd frontend
npm install
npm run dev
```

Full setup instructions and environment variables are in [`docs/setup.md`](docs/setup.md).

## Evaluation & Evidence of Value

We measure:

| Metric                        | Description                                      | Target (MVP)      |
|------------------------------|--------------------------------------------------|-------------------|
| Reconstruction Accuracy      | Correct ledger entries from messy inputs         | ≥ 85% on held-out |
| Human Confirmation Rate      | % of entries requiring merchant confirmation     | Tracked           |
| Answer Groundedness          | Answers that cite actual ledger sources          | ≥ 95%             |
| Action Proposal Precision    | Useful & safe action suggestions                 | Manual + auto     |
| Exception / Refusal Rate     | Cases the system correctly refuses to touch      | Honest list       |

Detailed evaluation methodology and results live in [`docs/metrics.md`](docs/metrics.md).

## What Broke & How We Fixed It

(This section will be filled with real failure stories during development — Razorpay specifically asks for it.)

## License

MIT (for the buildathon submission)

---

**Built for Razorpay AI Buildathon 2026 — Open Track**  
*Show a real problem. A working product. Meaningful use of AI. Evidence that it creates value.*
