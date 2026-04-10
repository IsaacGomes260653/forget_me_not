import os
import json
import pytest
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