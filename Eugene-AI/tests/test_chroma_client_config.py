from src.rag import retriever


def test_server_chroma_client_uses_http_and_token_auth(monkeypatch):
    captured = {}

    class FakeClient:
        def __init__(self, **kwargs):
            captured.update(kwargs)

        def get_collection(self, **kwargs):
            captured["collection"] = kwargs
            return "collection"

    monkeypatch.setattr(retriever.settings, "chroma_host", "chromadb.eugene-ai.svc.cluster.local")
    monkeypatch.setattr(retriever.settings, "chroma_port", 8001)
    monkeypatch.setattr(retriever.settings, "chroma_auth_token", "token")
    monkeypatch.setattr(retriever.settings, "chroma_auth_header", "Authorization")
    monkeypatch.setattr(retriever.chromadb, "HttpClient", FakeClient)

    assert retriever.get_collection() == "collection"
    assert captured["host"] == "chromadb.eugene-ai.svc.cluster.local"
    assert captured["port"] == 8001
    chroma_settings = captured["settings"]
    assert chroma_settings.chroma_client_auth_provider.endswith("TokenAuthClientProvider")
    assert chroma_settings.chroma_client_auth_credentials == "token"
    assert chroma_settings.chroma_auth_token_transport_header == "Authorization"
