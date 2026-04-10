import json
import os
from rich.console import Console
from rich.table import Table

console = Console()
ARQUIVO_JSON = "tasks.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def adicionar_tarefa(tarefas):
    nome = console.input("\n[bold cyan]📝 Descrição da tarefa:[/bold cyan] ")
    
    while True:
        console.print("\n[bold magenta]🎯 Níveis de Urgência:[/bold magenta]")
        console.print("1 - [bold red]Alta 🔴[/bold red] | 2 - [bold yellow]Média 🟡[/bold yellow] | 3 - [bold green]Baixa 🟢[/bold green]")
        opcao_urgencia = input("👉 Escolha (1, 2, ou 3): ")
        
        if opcao_urgencia == "1":
            urgencia = "Alta"
            break
        elif opcao_urgencia == "2":
            urgencia = "Média"
            break
        elif opcao_urgencia == "3":
            urgencia = "Baixa"
            break
        else:
            console.print("[bold red]❌ Opção inválida. Por favor, escolha 1, 2 ou 3.[/bold red]")
            
    tarefas.append({"nome": nome, "urgencia": urgencia, "concluida": False})
    console.print("\n[bold green]✨ Tarefa adicionada com sucesso! ✨[/bold green]")
    return tarefas

def listar_tarefas(tarefas):
    if not tarefas:
        console.print("\n[bold yellow]📭 Nenhuma tarefa cadastrada no momento. Que tal adicionar uma?[/bold yellow]")
        return

    table = Table(title="\n[bold magenta]:sparkles: Lista de Tarefas - ForgetMeNot :sparkles:[/bold magenta]")
    table.add_column("ID", justify="center", style="bold cyan")
    table.add_column("Tarefa", style="bold white")
    table.add_column("Urgência", justify="center")
    table.add_column("Status", justify="center")

    for i, t in enumerate(tarefas):
        status = "[bold green]✅ Concluída[/bold green]" if t.get("concluida") else "[bold red]⏳ Pendente[/bold red]"
        
        cor_urgencia = "white"
        urgencia_val = t.get("urgencia", "Baixa") 
        icone = ""
        
        if urgencia_val == "Alta":
            cor_urgencia = "bold red"
            icone = "🔴"
        elif urgencia_val in ["Média", "Media"]:
            cor_urgencia = "bold yellow"
            icone = "🟡"
        elif urgencia_val == "Baixa":
            cor_urgencia = "bold green"
            icone = "🟢"
            
        table.add_row(
            str(i), 
            t.get("nome", ""), 
            f"[{cor_urgencia}]{urgencia_val} {icone}[/{cor_urgencia}]", 
            status
        )

    console.print(table)

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return tarefas
        
    try:
        indice = int(input("\n👉 Digite o ID da tarefa para marcar como concluída: "))
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            nome_tarefa = tarefas[indice].get('nome', '')
            console.print(f"\n[bold green]🎉 Sucesso! A tarefa '{nome_tarefa}' foi concluída![/bold green]")
        else:
            console.print("[bold red]❌ ID inválido. Tarefa não encontrada.[/bold red]")
    except ValueError:
        console.print("[bold red]⚠️ Por favor, digite um número válido.[/bold red]")
    return tarefas

def deletar_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return tarefas

    try:
        indice = int(input("\n👉 Digite o ID da tarefa que deseja excluir: "))
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            nome_tarefa = tarefa_removida.get('nome', '')
            console.print(f"\n[bold green]🗑️ Tarefa '{nome_tarefa}' excluída para sempre![/bold green]")
        else:
            console.print("[bold red]❌ ID inválido. Tarefa não encontrada.[/bold red]")
    except ValueError:
        console.print("[bold red]⚠️ Por favor, digite um número válido.[/bold red]")
        
    return tarefas

def main():
    tarefas = carregar_tarefas()
    
    while True:
        console.print("\n[bold cyan]:rocket: --- Menu ForgetMeNot --- :rocket:[/bold cyan]")
        console.print("1. ➕ Adicionar Tarefa")
        console.print("2. 📋 Listar Tarefas")
        console.print("3. ✅ Concluir Tarefa")
        console.print("4. 🗑️ Deletar Tarefa")
        console.print("5. 🚪 Sair")
        
        opcao = input("\n👉 Escolha uma opção: ")
        
        if opcao == "1":
            tarefas = adicionar_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            tarefas = concluir_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "4":
            tarefas = deletar_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "5":
            console.print("\n[bold blue]👋 Saindo do ForgetMeNot. Até logo e seja produtivo![/bold blue]\n")
            break
        else:
            console.print("[bold red]❌ Opção inválida. Tente novamente.[/bold red]")

if __name__ == "__main__":
    main()
    