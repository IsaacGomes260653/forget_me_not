Markdown
# ForgetMeNot 🧠

**Autor:** Isaac Gomes  
**Repositório:** [https://github.com/IsaacGomes260653/forget_me_not](https://github.com/IsaacGomes260653/forget_me_not)  
**Versão:** 1.0.0

## Descrição do Projeto
O **ForgetMeNot** é um gerenciador de tarefas via linha de comando (CLI) desenvolvido para solucionar o problema da desorganização e do esquecimento de compromissos. A aplicação permite cadastrar afazeres com diferentes níveis de urgência, utilizando uma interface visual colorida que facilita a priorização das atividades diárias.

## Público-Alvo
Estudantes e profissionais que buscam uma ferramenta de produtividade minimalista, permitindo gerenciar tarefas diretamente do terminal de forma rápida e eficiente.

## Funcionalidades
* Cadastro de tarefas com descrição detalhada.
* Atribuição de prioridades (Alta, Média, Baixa) com destaque visual.
* Listagem em formato de tabela organizada.
* Persistência de dados local em arquivo JSON.
* Marcação de tarefas concluídas.

## Tecnologias Utilizadas
* **Python 3**: Linguagem base do projeto.
* **Rich**: Biblioteca para formatação visual e tabelas no terminal.
* **Pytest**: Framework para execução de testes unitários.
* **Flake8**: Ferramenta de linting para garantir a qualidade do código (PEP 8).
* **GitHub Actions**: Implementação de pipeline de CI (Integração Contínua).

## Instalação e Uso
1. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
Execute a aplicação:

Bash
python src/main.py
Testes e Qualidade
Para validar o código e garantir que não existam erros de estilo ou lógica, execute:

Executar suíte de testes:

Bash
python -m pytest tests/
Verificar padrão de código (Linting):

Bash
python -m flake8 src/
Integração Contínua (CI)
O projeto utiliza GitHub Actions. A cada atualização (push), uma pipeline automática é disparada para instalar dependências, rodar o linter e executar os testes, assegurando a integridade da branch principal.


---

### Comandos para atualizar o GitHub agora:

Após salvar o arquivo acima no VSCode, execute estes comandos no seu terminal para garantir que o tempo de atualização mude no GitHub:

```bash
git add README.md
git commit -m "docs: finaliza readme conforme requisitos academicos"
git push
