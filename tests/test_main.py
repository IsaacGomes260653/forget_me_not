import os
import json
import pytest
import requests
from unittest.mock import patch, Mock
from src.main import carregar_tarefas, salvar_tarefas, FILE_PATH

TEST_FILE_PATH = "test_tasks.json"

@pytest.fixture(autouse=True)
def setup_e_teardown():
    import src.main
    src.main.FILE_PATH = TEST_FILE_PATH
    
    with open(TEST_FILE_PATH, "w", encoding="utf-8") as f:
        json.dump([], f)
        
    yield 
    
    if os.path.exists(TEST_FILE_PATH):
        os.remove(TEST_FILE_PATH)

def test_salvar_e_carregar_tarefas():
    tarefas_teste = [{"nome": "Estudar Python", "urgencia": "Alta", "concluida": False}]
    salvar_tarefas(tarefas_teste)
    tarefas_carregadas = carregar_tarefas()
    
    assert len(tarefas_carregadas) == 1
    assert tarefas_carregadas[0]["nome"] == "Estudar Python"
    assert tarefas_carregadas[0]["concluida"] is False

def test_adicionar_tarefa_logica():
    tarefas = []
    nova_tarefa = {"nome": "Beber agua", "urgencia": "Media", "concluida": False}
    tarefas.append(nova_tarefa)
    
    assert len(tarefas) == 1
    assert tarefas[0]["nome"] == "Beber agua"
    assert tarefas[0]["urgencia"] == "Media"

def test_concluir_tarefa_logica():
    tarefas = [{"nome": "Pagar conta", "urgencia": "Alta", "concluida": False}]
    tarefas[0]["concluida"] = True
    assert tarefas[0]["concluida"] is True


# ─── TESTES DE INTEGRAÇÃO ────────────────────────────────────────────────────

def test_api_advice_retorna_status_200():
    """Integração real: verifica que a API responde com sucesso."""
    response = requests.get("https://api.adviceslip.com/advice", timeout=5)
    assert response.status_code == 200

def test_api_advice_retorna_json_valido():
    """Integração real: verifica que o JSON tem a estrutura esperada."""
    response = requests.get("https://api.adviceslip.com/advice", timeout=5)
    data = response.json()
    assert "slip" in data
    assert "advice" in data["slip"]
    assert isinstance(data["slip"]["advice"], str)
    assert len(data["slip"]["advice"]) > 0

def test_buscar_dica_mock():
    """Mock: valida que buscar_dica() processa corretamente a resposta da API."""
    from src.app import buscar_dica

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "slip": {"id": 1, "advice": "Dica de teste mocada com sucesso."}
    }

    with patch("src.app.requests.get", return_value=mock_response):
        dica = buscar_dica()

    assert dica == "Dica de teste mocada com sucesso."

def test_buscar_dica_fallback_quando_api_falha():
    """Mock: valida que buscar_dica() retorna mensagem padrão se a API cair."""
    from src.app import buscar_dica

    with patch("src.app.requests.get", side_effect=Exception("Sem conexão")):
        dica = buscar_dica()

    assert dica == "Foque no que importa: uma tarefa de cada vez."