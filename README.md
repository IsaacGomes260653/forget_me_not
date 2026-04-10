Markdown
# 🧠 ForgetMeNot

> *Seu assistente de terminal para organizar as semanas de prova e não deixar nenhuma entrega passar!* 🚀

**🧑‍💻 Desenvolvido por:** Isaac Gomes  
**🔗 Repositório:** [https://github.com/IsaacGomes260653/forget_me_not](https://github.com/IsaacGomes260653/forget_me_not)  
**🏷️ Versão:** 1.0.0

---

## 💡 Qual é a ideia?
Sabe aquela rotina cheia de fim de semestre, trabalho misturado com projeto da faculdade, em que a gente acaba perdendo a noção do que precisa entregar primeiro? O **ForgetMeNot** nasceu para resolver isso. Ele é um gerenciador de tarefas que roda direto no terminal (CLI). Sem interfaces pesadas ou necessidade de abrir mais uma aba no navegador: apenas o terminal colorido e direto ao ponto para você focar no que realmente importa.

## 🎯 Para quem é isso?
Para estudantes e desenvolvedores que já passam o dia todo com o terminal aberto e querem organizar as prioridades da rotina sem sair do ambiente de código.

## ✨ O que ele faz?
* ➕ **Adiciona na hora:** Lembrou da tarefa, cadastrou.
* 🚦 **Prioridade visual:** Para você bater o olho e saber exatamente o que é mais urgente (🔴 Alta, 🟡 Média, 🟢 Baixa).
* 📊 **Tabela organizada:** A gente gosta de usar o terminal, mas ele não precisa ser uma tela preta sem graça.
* 💾 **Não perde nada:** Salva tudo de forma segura em um arquivo JSON. Pode fechar o programa tranquilo que seus dados continuam lá.
* ✅ **Conclusão de tarefas:** Aquela sensação boa de dar o "check" e marcar a atividade como finalizada.
* 🗑️ **Exclusão:** Cadastrou errado ou a tarefa foi cancelada? É só deletar (CRUD completo implementado!).

## 🛠️ O que roda por baixo dos panos (Tecnologias)
* **🐍 Python 3:** A linguagem base do projeto.
* **🎨 Rich:** A biblioteca que faz a mágica das cores, emojis e tabelas no terminal.
* **🧪 Pytest:** Testes unitários para garantir que o código não vai quebrar de surpresa.
* **🧹 Flake8:** Ferramenta de linting para manter o código limpo e nos padrões de mercado (PEP 8).
* **⚙️ GitHub Actions:** Automação de testes rodando direto na nuvem.

---

## 🚀 Como rodar o projeto

**1. Instale as dependências:**
```bash
pip install -r requirements.txt
2. Inicie a aplicação:

Bash
python src/main.py
🧪 Como testar a qualidade do código
Se quiser ver os bastidores e conferir se a qualidade está no padrão esperado, execute os comandos abaixo:

Para rodar os testes automatizados:

Bash
python -m pytest tests/
Para verificar a formatação do código (Linting):

Bash
python -m flake8 src/
🔄 Automação (CI/CD)
Este repositório conta com uma pipeline do GitHub Actions configurada. Sempre que enviamos uma atualização (push), o servidor instala as dependências, analisa o código com o Flake8 e executa os testes do Pytest automaticamente. Se o ícone do commit ficar verde, a atualização foi um sucesso! 🎉


---

### Para enviar essa versão perfeita para o GitHub:

Basta salvar o arquivo no VSCode (**Ctrl + S**) e rodar os três comandos no terminal:

```bash
git add README.md
git commit -m "docs: Atualizar o código para testar"
git push