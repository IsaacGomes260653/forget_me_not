import json
import os
import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"))

FILE_PATH = "tasks.json"


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


@app.route("/")
def index():
    tarefas = carregar_tarefas()
    dica = buscar_dica()
    return render_template("index.html", tarefas=tarefas, dica=dica)


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
