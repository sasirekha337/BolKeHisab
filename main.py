"""
BolKeHisab — Voice-First Living Ledger
Razorpay AI Buildathon 2026 — Open Track
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ingest import router as ingest_router
from ledger import router as ledger_router
from agent import router as agent_router

app = FastAPI(
    title="BolKeHisab",
    description="Voice-First Living Ledger for India’s Informal Merchants",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest_router, prefix="/ingest", tags=["Ingest"])
app.include_router(ledger_router, prefix="/ledger", tags=["Ledger"])
app.include_router(agent_router, prefix="/agent", tags=["Agent"])


@app.get("/")
def root():
    return {
        "project": "BolKeHisab",
        "track": "Razorpay AI Buildathon 2026 — Open Track",
        "message": "Voice-First Living Ledger for India’s Informal Merchants",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "ok", "service": "BolKeHisab"}
