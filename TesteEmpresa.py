from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_empresa():
    response = client.post("/empresas/", json={
        "id": 12312319,
        "nome": "Empresa Teste",
        "cnpj": "12345678000156",
        "endereco": "Rua Teste, 123",
        "email": "empresa@teste.com",
        "telefone": 123456789
    })
    
    assert response.status_code == 201  # Verifica se a resposta foi bem-sucedida
    data = response.json()
    assert data["nome"] == "Empresa Teste"
    assert data["cnpj"] == "12345678000158"
