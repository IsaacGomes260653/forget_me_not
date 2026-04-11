Markdown
# 🚀 ForgetMeNot - Sistema de Gestão de Tarefas

## 📝 Introdução
O **ForgetMeNot** é um gerenciador de tarefas (To-Do List) desenvolvido em Python, focado em simplicidade e usabilidade via terminal. O projeto foi criado como parte de um trabalho acadêmico para demonstrar a aplicação de conceitos de programação, persistência de dados em arquivos JSON, testes automatizados e integração contínua (CI).

O diferencial do sistema é a utilização da biblioteca `rich`, que proporciona uma interface visual organizada e colorida, tornando a experiência no terminal muito mais intuitiva para o utilizador.

---

## 👤 Autor
* **Isaac Gomes**
* **Repositório:** [https://github.com/IsaacGomes260653/forget_me_not](https://github.com/IsaacGomes260653/forget_me_not)

---

## ✨ Funcionalidades
- **Adicionar Tarefas:** Registo de tarefas com descrição e três níveis de urgência (Alta, Média, Baixa).
- **Listagem Interativa:** Visualização de tarefas numa tabela organizada com cores e ícones.
- **Conclusão de Tarefas:** Marcação de itens concluídos com atualização de status.
- **Exclusão de Tarefas:** Remoção de itens da lista de forma simples.
- **Persistência de Dados:** Todas as tarefas são guardadas automaticamente num ficheiro `tasks.json`.
- **Qualidade de Código:** Cobertura de testes com `pytest` e verificação de padrões de código com `flake8`.

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.11+
- **Interface:** [Rich Library](https://github.com/Textualize/rich)
- **Testes:** Pytest
- **CI/CD:** GitHub Actions (Pipeline de testes e linting automatizada)

---

## ⚠️ Pré-requisitos: Como instalar o Python
Para executar este projeto, é necessário ter o **Python 3.x** instalado na sua máquina. Caso ainda não tenha, siga o passo a passo abaixo de acordo com o seu sistema operacional:

**🪟 Windows:**
1. Acesse o site oficial: [python.org/downloads](https://www.python.org/downloads/)
2. Clique no botão amarelo "Download Python 3.x.x" para baixar a versão mais recente.
3. Abra o arquivo executável que foi baixado.
4. **MUITO IMPORTANTE:** Na primeira tela do instalador, marque a opção **"Add python.exe to PATH"** na parte inferior da janela.
5. Clique em *Install Now* e aguarde a conclusão.

**🍎 macOS:**
1. Acesse [python.org/downloads](https://www.python.org/downloads/) e baixe o instalador para macOS.
2. Execute o arquivo baixado e siga as instruções na tela até o fim.
*(Alternativa para usuários avançados via Homebrew: abra o terminal e digite `brew install python`)*

**🐧 Linux (Ubuntu/Debian):**
A maioria das distribuições Linux já vem com o Python pré-instalado. Para garantir que possui a versão 3 e o gerenciador de pacotes (`pip`), abra o terminal e execute:
```bash
sudo apt update
sudo apt install python3 python3-pip
🚀 Como instalar e executar o projeto
1. Clonar o repositório
Abra o seu terminal e baixe o projeto rodando o comando:

Bash
git clone [https://github.com/IsaacGomes260653/forget_me_not.git](https://github.com/IsaacGomes260653/forget_me_not.git)
2. Acessar a pasta do projeto

Bash
cd forget_me_not
3. Instalar as dependências
O projeto utiliza a biblioteca rich para renderizar a interface no terminal. Para instalá-la, execute:

Bash
pip install rich
4. Executar o aplicativo
Com tudo instalado, inicie o gerenciador de tarefas com o comando:

Bash
python src/main.py
🧪 Testes e Integração Contínua (CI)
Este projeto possui testes automatizados e integração contínua (CI) configurados via GitHub Actions. Sempre que um novo código é enviado (push), o servidor verifica automaticamente a padronização do código (Flake8) e executa os testes unitários (Pytest).

Para rodar os testes localmente na sua máquina, instale o pytest e execute:

Bash
pip install pytest
python -m pytest tests/