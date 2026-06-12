"""Role-filtered ChromaDB retrieval for Eugene."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import chromadb
from chromadb.config import Settings as ChromaSettings

from config.settings import settings
from src.guardrails.access_control import filter_chunks_by_tier
from src.rag.document_store import OllamaEmbeddingFunction, embed_text


def get_collection():
    if settings.chroma_host not in {"localhost", "127.0.0.1", ""}:
        chroma_settings = ChromaSettings(anonymized_telemetry=False)
        if settings.chroma_auth_token:
            chroma_settings = ChromaSettings(
                anonymized_telemetry=False,
                chroma_client_auth_provider="chromadb.auth.token_authn.TokenAuthClientProvider",
                chroma_client_auth_credentials=settings.chroma_auth_token,
                chroma_auth_token_transport_header=settings.chroma_auth_header,
            )
        client = chromadb.HttpClient(
            host=settings.chroma_host,
            port=settings.chroma_port,
            settings=chroma_settings,
        )
        return client.get_collection(
            name=settings.chroma_collection,
            embedding_function=OllamaEmbeddingFunction(),
        )

    client = chromadb.PersistentClient(
        path=str(settings.chroma_persist_path),
        settings=ChromaSettings(anonymized_telemetry=False, allow_reset=True),
    )
    return client.get_collection(
        name=settings.chroma_collection,
        embedding_function=OllamaEmbeddingFunction(),
    )


def retrieve(query: str, role: str, *, top_k: int | None = None) -> list[dict]:
    """Return role-approved chunks with source metadata."""
    collection = get_collection()
    query_embedding = embed_text(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k or settings.query_top_k,
        include=["documents", "metadatas", "distances"],
    )
    chunks: list[dict] = []
    ids = results.get("ids", [[]])[0]
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]
    for index, chunk_id in enumerate(ids):
        metadata = metadatas[index] or {}
        chunks.append(
            {
                "id": chunk_id,
                "text": documents[index],
                "distance": distances[index] if index < len(distances) else None,
                **metadata,
            }
        )
    return filter_chunks_by_tier(chunks, role)


def _main() -> int:
    parser = argparse.ArgumentParser(description="Query Eugene's RAG corpus.")
    parser.add_argument("query", nargs="?", default="Who is the CISO at MedData Nexus?")
    parser.add_argument("--role", default="it_security")
    parser.add_argument("--top-k", type=int, default=settings.query_top_k)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    chunks = retrieve(args.query, args.role, top_k=args.top_k)
    payload = {"query": args.query, "role": args.role, "chunks": chunks}
    if args.output:
        args.output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
