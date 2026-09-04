# Setup Guide — BolKeHisab

## Prerequisites

- Python 3.11+
- Node.js 18+ (for frontend)
- ffmpeg (for audio processing)
- Git

## Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
# Edit .env with your API keys (optional for local mocks)
```

### Environment Variables

```env
# Core
DATABASE_URL=sqlite:///./bolkehisab.db
SECRET_KEY=change-me-in-production

# AI Providers (leave empty to use mocks for demo)
OPENAI_API_KEY=
GROQ_API_KEY=
# or local model endpoints

# Razorpay Test Mode (for payment link generation)
RAZORPAY_KEY_ID=
RAZORPAY_KEY_SECRET=

# Feature flags
USE_MOCK_STT=true
USE_MOCK_VISION=true
USE_MOCK_LLM=true
```

### Run Backend

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API docs: http://localhost:8000/docs

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Usually available at http://localhost:5173

## Demo Mode

For the 5-minute pitch and judges who may not have API keys:

- Set all `USE_MOCK_*=true`
- The system uses high-quality synthetic responses that still exercise the full ledger + policy + provenance path
- Real AI providers can be enabled later without changing the core architecture

## Evaluation Scripts

```bash
cd scripts
python evaluate_reconstruction.py --dataset ../data/synthetic/held_out.json
```

This produces the accuracy and exception metrics required for the submission.
