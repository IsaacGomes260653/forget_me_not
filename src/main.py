import json
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()
FILE_PATH = "tasks.json"


def carregar_tarefas():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def salvar_tarefas(tarefas):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(tarefas, file, indent=4)


def adicionar_tarefa(tarefas):
    console.print("\n[bold cyan]--- Nova Tarefa ---[/bold cyan]")
    nome = Prompt.ask("O que você precisa lembrar de fazer?")
    urgencia = Prompt.ask(
        "Qual a urgência?",
        choices=[
            "Alta",
            "Media",
            "Baixa"],
        default="Media")

    nova_tarefa = {"nome": nome, "urgencia": urgencia, "concluida": False}
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    console.print(f"[green]✔ Tarefa '{nome}' adicionada com sucesso![/green]")


def listar_tarefas(tarefas):
    console.print("\n")
    if not tarefas:
        console.print(
            "[yellow]Sua lista está vazia. Aproveite o descanso![/yellow]")
        return

    tabela = Table(title="📋 Minhas Tarefas - ForgetMeNot")
    tabela.add_column("ID", justify="center", style="cyan")
    tabela.add_column("Tarefa", style="white")
    tabela.add_column("Urgência", justify="center")
    tabela.add_column("Status", justify="center")

    for idx, tarefa in enumerate(tarefas):
        cor = "green"
        if tarefa["urgencia"] == "Alta":
            cor = "bold red"
        elif tarefa["urgencia"] == "Media":
            cor = "yellow"

        status = "[green]✔ Concluída[/green]" if tarefa["concluida"] else "[red]✖ Pendente[/red]"
        tabela.add_row(str(idx + 1),
                       tarefa["nome"],
                       f"[{cor}]{tarefa['urgencia']}[/{cor}]",
                       status)

    console.print(tabela)


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        console.print("\n")
        id_escolhido = int(
            Prompt.ask("Digite o ID da tarefa que deseja concluir")) - 1
        if 0 <= id_escolhido < len(tarefas):
            tarefas[id_escolhido]["concluida"] = True
            salvar_tarefas(tarefas)
            console.print("[green]✔ Mandou bem! Tarefa concluída.[/green]")
        else:
            console.print("[red]✖ ID não encontrado.[/red]")
    except ValueError:
        console.print("[red]✖ Por favor, digite apenas números.[/red]")


def main():
    console.print("\n[bold blue]🧠 Bem-vindo ao ForgetMeNot![/bold blue]")
    tarefas = carregar_tarefas()

    while True:
        console.print(
            "\n[1] Adicionar Tarefa  [2] Listar Tarefas  [3] Concluir Tarefa  [4] Sair")
        escolha = Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4"])

        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            concluir_tarefa(tarefas)
        elif escolha == "4":
            console.print(
                "[bold blue]Até logo e mantenha o foco![/bold blue]\n")
            break


if __name__ == "__main__":
    main()
