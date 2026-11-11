import json
from datetime import datetime, timezone
from unittest.mock import patch

import pytest

import src.app


# 22h de 11/11/2026 em Brasília (UTC-3) já é 01h de 12/11/2026 em UTC.
AS_22H_EM_BRASILIA = datetime(2026, 11, 12, 1, 0, tzinfo=timezone.utc)


@pytest.fixture
def pagina(tmp_path, monkeypatch):
    """Monta a página com as tarefas dadas, num arquivo temporário e sem chamar a API."""
    arquivo = tmp_path / "tasks.json"
    monkeypatch.setattr(src.app, "FILE_PATH", str(arquivo))
    monkeypatch.setattr(src.app, "buscar_dica", lambda: "Dica de teste.")

    def montar(tarefas):
        arquivo.write_text(json.dumps(tarefas), encoding="utf-8")
        return src.app.app.test_client().get("/").get_data(as_text=True)

    return montar


def test_prazo_de_hoje_as_22h_em_brasilia_vence_hoje(pagina):
    """Às 22h em Brasília, uma tarefa que vence no mesmo dia ainda não venceu."""
    with patch("src.app.agora", return_value=AS_22H_EM_BRASILIA):
        html = pagina([{"nome": "Entregar o relatório", "urgencia": "Alta", "concluida": False, "prazo": "2026-11-11"}])

    assert "Vence hoje!" in html
    assert "Vencido" not in html


def test_prazo_de_ontem_as_22h_em_brasilia_esta_vencido(pagina):
    with patch("src.app.agora", return_value=AS_22H_EM_BRASILIA):
        html = pagina([{"nome": "Pagar a conta", "urgencia": "Alta", "concluida": False, "prazo": "2026-11-10"}])

    assert "Vencido em 10/11/2026" in html


def test_prazo_de_amanha_as_22h_em_brasilia_esta_no_prazo(pagina):
    with patch("src.app.agora", return_value=AS_22H_EM_BRASILIA):
        html = pagina([{"nome": "Revisar o código", "urgencia": "Média", "concluida": False, "prazo": "2026-11-12"}])

    assert "12/11/2026" in html
    assert "Vence hoje!" not in html
    assert "Vencido" not in html
