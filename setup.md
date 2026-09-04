# Setup Guide — BolKeHisab

## Requirements

- Python 3.10 or higher

## Run the Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Open in browser: http://localhost:8000/docs

## Demo Mode

The current version runs in demo mode with mock responses.
It still exercises the full policy engine, ledger models, and agent flow.

## Next Steps for Full Version

- Connect real Speech-to-Text
- Connect OCR / Vision model
- Add persistent database
- Build simple chat frontend
