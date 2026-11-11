import json
import os
from datetime import date, datetime, timezone
from zoneinfo import ZoneInfo

import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"))

FILE_PATH = "tasks.json"
FUSO = ZoneInfo("America/Sao_Paulo")


def carregar_tarefas():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_tarefas(tarefas):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)


def buscar_dica():
    try:
        response = requests.get(
            "https://api.adviceslip.com/advice", timeout=5
        )
        response.raise_for_status()
        data = response.json()
        return data["slip"]["advice"]
    except Exception:
        return "Foque no que importa: uma tarefa de cada vez."


def agora():
    return datetime.now(timezone.utc)


def hoje():
    """A data de hoje no horário de Brasília, seja qual for o fuso do servidor."""
    return agora().astimezone(FUSO).date()


@app.template_filter("situacao_prazo")
def situacao_prazo(prazo, dia):
    """'vencido', 'hoje' ou 'ok' para um prazo AAAA-MM-DD; None sem prazo válido."""
    try:
        data = date.fromisoformat(prazo)
    except (TypeError, ValueError):
        return None
    if data < dia:
        return "vencido"
    if data == dia:
        return "hoje"
    return "ok"


@app.template_filter("data_br")
def data_br(prazo):
    """AAAA-MM-DD vira DD/MM/AAAA; qualquer outra coisa volta como veio."""
    try:
        return date.fromisoformat(prazo).strftime("%d/%m/%Y")
    except (TypeError, ValueError):
        return prazo


@app.route("/")
def index():
    tarefas = carregar_tarefas()
    dica = buscar_dica()
    return render_template("index.html", tarefas=tarefas, dica=dica, hoje=hoje())


@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form.get("nome", "").strip()
    urgencia = request.form.get("urgencia", "Baixa")
    prazo = request.form.get("prazo", "")
    if nome:
        tarefas = carregar_tarefas()
        tarefas.append({"nome": nome, "urgencia": urgencia, "concluida": False, "prazo": prazo})
        salvar_tarefas(tarefas)
    return redirect(url_for("index"))


@app.route("/concluir/<int:indice>")
def concluir(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
    return redirect(url_for("index"))


@app.route("/deletar/<int:indice>")
def deletar(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        salvar_tarefas(tarefas)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
