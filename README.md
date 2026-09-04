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

1. **Multimodal Intake** — Accepts voice notes, photos of handwritten diaries, UPI screenshots, and chat text.
2. **Living Ledger** — Reconstructs a clean, double-entry style ledger with full provenance for every entry.
3. **Natural Language Interface** — Merchants ask questions in everyday Hinglish and get grounded answers.
4. **Bounded Agent Actions** — Proposes high-value next steps (generate Razorpay payment link, draft collection message, flag shortfall) — never executes money movement without explicit human confirmation.
5. **Audit & Trust** — Every number is traceable. Low-confidence items are gated. The system prefers saying “I don’t know” over inventing figures.

## Architecture Overview

```
Multimodal Intake (Voice • Photo • Text)
        ↓
Perception Layer (STT + OCR + Extraction)
        ↓
Living Ledger Engine (Deterministic + Provenance)
        ↓
Bounded Agent (Policy Engine above LLM)
```

See `docs/architecture.md` for detailed design decisions and guardrails.

## Key Design Principles

- **AI is a tool, not the source of truth** — deterministic ledger + policy engine sit above the models.
- **Provenance over perfection** — every entry must explain where it came from.
- **Human-in-the-loop by default** for any low-confidence or money-adjacent action.
- **Culturally native interface** — voice + photo first, not dashboard first.
- **Honest metrics** — we publish reconstruction accuracy, exception rates, and failure cases.

## Project Structure

```
BolKeHisab/
├── backend/           # FastAPI application
│   ├── main.py
│   ├── policy.py
│   ├── ledger.py
│   ├── ingest.py
│   ├── agent.py
│   └── requirements.txt
├── docs/
│   ├── architecture.md
│   └── setup.md
└── README.md
```

## Quick Start

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

API docs will be available at: http://localhost:8000/docs

## Evaluation Metrics (Target)

| Metric                        | Target      |
|------------------------------|-------------|
| Reconstruction Accuracy      | ≥ 85%       |
| Answer Groundedness          | ≥ 95%       |
| Human Confirmation Rate      | Tracked     |
| Exception / Refusal Rate     | Honest list |

## What Broke & How We Fixed It

(To be filled with real development stories)

---

**Built for Razorpay AI Buildathon 2026 — Open Track**  
*Show a real problem. A working product. Meaningful use of AI. Evidence that it creates value.*
