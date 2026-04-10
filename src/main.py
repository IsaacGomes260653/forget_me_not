import json
import os
from rich.console import Console
from rich.table import Table

console = Console()
ARQUIVO_JSON = "tarefas.json"

def carregar_tarefas():
    """Carrega as tarefas salvas no arquivo JSON."""
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa com nível de prioridade."""
    descricao = input("Descrição da tarefa: ")
    print("Prioridades: 1 - Alta | 2 - Média | 3 - Baixa")
    opcao_prioridade = input("Escolha a prioridade: ")
    
    prioridade = "Baixa"
    if opcao_prioridade == "1":
        prioridade = "Alta"
    elif opcao_prioridade == "2":
        prioridade = "Média"
        
    tarefas.append({"descricao": descricao, "prioridade": prioridade, "concluida": False})
    console.print("[bold green]Tarefa adicionada com sucesso![/bold green]")
    return tarefas

def listar_tarefas(tarefas):
    """Lista as tarefas em uma tabela formatada."""
    if not tarefas:
        console.print("[bold yellow]Nenhuma tarefa cadastrada no momento.[/bold yellow]")
        return

    table = Table(title="Lista de Tarefas - ForgetMeNot")
    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Descrição", style="white")
    table.add_column("Prioridade", justify="center")
    table.add_column("Status", justify="center")

    for i, t in enumerate(tarefas):
        status = "[green]Concluída[/green]" if t["concluida"] else "[red]Pendente[/red]"
        
        # Define a cor baseada na prioridade
        cor_prioridade = "white"
        if t["prioridade"] == "Alta":
            cor_prioridade = "bold red"
        elif t["prioridade"] == "Média":
            cor_prioridade = "bold yellow"
        elif t["prioridade"] == "Baixa":
            cor_prioridade = "bold green"
            
        table.add_row(str(i), t["descricao"], f"[{cor_prioridade}]{t['prioridade']}[/{cor_prioridade}]", status)

    console.print(table)

def concluir_tarefa(tarefas):
    """Marca uma tarefa existente como concluída."""
    listar_tarefas(tarefas)
    if not tarefas:
        return tarefas
        
    try:
        indice = int(input("\nDigite o ID da tarefa para marcar como concluída: "))
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            console.print(f"[bold green]Tarefa '{tarefas[indice]['descricao']}' concluída![/bold green]")
        else:
            console.print("[bold red]ID inválido. Tarefa não encontrada.[/bold red]")
    except ValueError:
        console.print("[bold red]Por favor, digite um número válido.[/bold red]")
    return tarefas

def deletar_tarefa(tarefas):
    """Remove uma tarefa da lista pelo seu ID."""
    listar_tarefas(tarefas)
    if not tarefas:
        return tarefas

    try:
        indice = int(input("\nDigite o ID da tarefa que deseja excluir: "))
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            console.print(f"[bold green]Tarefa '{tarefa_removida['descricao']}' excluída com sucesso![/bold green]")
        else:
            console.print("[bold red]ID inválido. Tarefa não encontrada.[/bold red]")
    except ValueError:
        console.print("[bold red]Por favor, digite um número válido.[/bold red]")
        
    return tarefas

def main():
    """Função principal que gerencia o menu da aplicação."""
    tarefas = carregar_tarefas()
    
    while True:
        console.print("\n[bold blue]--- Menu ForgetMeNot ---[/bold blue]")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Deletar Tarefa")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
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
            console.print("[bold blue]Saindo do ForgetMeNot. Até logo![/bold blue]")
            break
        else:
            console.print("[bold red]Opção inválida. Tente novamente.[/bold red]")

if __name__ == "__main__":
    main()