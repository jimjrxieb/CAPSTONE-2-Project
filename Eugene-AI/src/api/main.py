"""FastAPI application. Docs endpoint disabled in production."""
from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings
from src.api.routes import query, evidence, ingest

# Disable docs in production
docs_url = None if settings.disable_docs else "/docs"
redoc_url = None if settings.disable_docs else "/redoc"


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings.validate()
    yield


app = FastAPI(
    title="Eugene-AI Assessment API",
    version="0.1.0",
    docs_url=docs_url,
    redoc_url=redoc_url,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(query.router, prefix="/query", tags=["query"])
app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
app.include_router(evidence.router, prefix="/evidence", tags=["evidence"])


@app.middleware("http")
async def add_security_headers(request, call_next) -> Response:
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
