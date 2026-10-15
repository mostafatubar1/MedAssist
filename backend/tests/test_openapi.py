def test_health_and_swagger_contract_available(client):
    assert client.get("/health").json() == {"status": "ok"}
    openapi = client.get("/openapi.json")
    assert openapi.status_code == 200
    assert "/api/auth/login" in openapi.json()["paths"]
    assert "/api/rag/questions" in openapi.json()["paths"]
