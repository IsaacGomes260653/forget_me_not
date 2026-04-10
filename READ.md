ForgetMeNot 🧠
Autor: Isaac Gomes

Repositório: https://github.com/IsaacGomes260653/forget_me_not

Versão: 1.0.0

Descrição do Projeto
O ForgetMeNot é um gerenciador de tarefas via linha de comando (CLI) focado em resolver o problema da desorganização diária. A aplicação permite que o usuário cadastre seus afazeres e defina níveis de urgência, ajudando na priorização visual das atividades e evitando o esquecimento de compromissos importantes.

Público-Alvo
Estudantes e profissionais que utilizam o terminal em sua rotina e precisam de uma ferramenta rápida e leve para organizar listas de tarefas sem sair do ambiente de desenvolvimento.

Funcionalidades
Cadastro de tarefas com descrição.

Atribuição de níveis de prioridade (Alta, Média, Baixa).

Listagem organizada em tabela com cores.

Persistência de dados em arquivo JSON.

Marcação de conclusão de tarefas.

Tecnologias
Python 3

Biblioteca Rich (Interface)

Pytest (Testes)

Flake8 (Linting)

GitHub Actions (CI)

Instalação e Uso
Instale as dependências:

Bash
pip install -r requirements.txt
Inicie o programa:

Bash
python src/main.py
Testes e Qualidade
Para garantir o funcionamento e a padronização do código, utilize os comandos abaixo:

Executar testes:

Bash
python -m pytest tests/
Verificar estilo (Linting):

Bash
python -m flake8 src/
Integração Contínua (CI)
O projeto conta com um workflow do GitHub Actions que valida automaticamente cada push realizado. O processo instala as dependências e executa o Linting e os Testes para assegurar que a versão no repositório esteja sempre estável.