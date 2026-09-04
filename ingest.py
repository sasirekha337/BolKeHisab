from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
from datetime import datetime
import uuid

router = APIRouter()


@router.post("/voice")
async def ingest_voice(
    file: UploadFile = File(...),
    merchant_id: str = Form("demo-merchant"),
    note: Optional[str] = Form(None),
):
    event_id = str(uuid.uuid4())
    return {
        "event_id": event_id,
        "type": "voice",
        "merchant_id": merchant_id,
        "filename": file.filename,
        "status": "accepted",
        "message": "Voice note received. Transcription + extraction queued.",
        "received_at": datetime.utcnow().isoformat(),
    }


@router.post("/photo")
async def ingest_photo(
    file: UploadFile = File(...),
    merchant_id: str = Form("demo-merchant"),
):
    event_id = str(uuid.uuid4())
    return {
        "event_id": event_id,
        "type": "photo",
        "merchant_id": merchant_id,
        "filename": file.filename,
        "status": "accepted",
        "message": "Photo received. OCR + layout extraction queued.",
        "received_at": datetime.utcnow().isoformat(),
    }


@router.post("/text")
async def ingest_text(
    text: str = Form(...),
    merchant_id: str = Form("demo-merchant"),
):
    event_id = str(uuid.uuid4())
    return {
        "event_id": event_id,
        "type": "text",
        "merchant_id": merchant_id,
        "text_preview": text[:120],
        "status": "accepted",
        "message": "Text received. Extraction queued.",
        "received_at": datetime.utcnow().isoformat(),
    }
