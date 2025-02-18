from fastapi.testclient import TestClient  
from main import app  

client = TestClient(app)  

def test_create_obrigacao():  
    response = client.post("/obrigacoes/", json={  
        "id": 12311,  
        "nome": "Declaracao Anual",  
        "periodicidade": "mensal",  
        "fk_empresa": 12312319
    })  
    
    assert response.status_code == 201  
    data = response.json()  
    assert data["nome"] == "Declaracao Anual"  
    assert data["periodicidade"] == "mensal"  
    assert data["fk_empresa"] == 12312319