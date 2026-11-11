<p align="center">
  <picture>
    <source media="(max-width: 767px)" srcset="https://raw.githubusercontent.com/IsaacGomes260653/forget_me_not/main/.github/banner-mobile.svg">
    <img src="https://raw.githubusercontent.com/IsaacGomes260653/forget_me_not/main/.github/banner.svg" alt="ForgetMeNot, trabalho acadêmico no ar no Render: tarefas com urgência e prazo, no navegador ou no terminal, com testes e CI no GitHub Actions">
  </picture>
</p>

<p align="center">
  <b>Lista de tarefas em Python e Flask em que cada tarefa tem urgência e prazo, e a página avisa o que já venceu e o que vence hoje.</b><br>
  Para quem quer anotar tarefas sem criar conta, e para quem estuda Flask e quer ver um app pequeno com testes, CI e deploy.<br>
  <a href="https://forget-me-not-z9hy.onrender.com"><b>Abrir a demonstração</b></a> · no plano gratuito do Render, o primeiro acesso leva cerca de 30 segundos
</p>

<p align="center">
  <a href="https://github.com/IsaacGomes260653/forget_me_not/actions/workflows/ci.yml"><img alt="Status da CI" src="https://img.shields.io/github/actions/workflow/status/IsaacGomes260653/forget_me_not/ci.yml?branch=main&style=flat-square&label=CI&color=122039&labelColor=0b1324"></a>
  <a href="LICENSE"><img alt="Licença MIT" src="https://img.shields.io/github/license/IsaacGomes260653/forget_me_not?style=flat-square&label=licen%C3%A7a&color=122039&labelColor=0b1324"></a>
  <a href="https://github.com/IsaacGomes260653/forget_me_not/commits/main"><img alt="Data do último commit" src="https://img.shields.io/github/last-commit/IsaacGomes260653/forget_me_not?style=flat-square&label=%C3%BAltimo%20commit&color=122039&labelColor=0b1324"></a>
  <img alt="Linguagem principal: Python" src="https://img.shields.io/github/languages/top/IsaacGomes260653/forget_me_not?style=flat-square&logo=python&logoColor=white&color=122039&labelColor=0b1324">
</p>

<p align="center">
  <a href="#demonstração">Demonstração</a> ·
  <a href="#como-rodar-em-60-segundos">Como rodar</a> ·
  <a href="#o-que-ele-faz">O que ele faz</a> ·
  <a href="#como-foi-feito">Como foi feito</a> ·
  <a href="#testes-e-qualidade">Testes e CI</a> ·
  <a href="#próximos-passos">Próximos passos</a> ·
  <a href="#english-summary">English</a>
</p>

## Demonstração

<p align="center">
  <img src=".github/capturas/demo.gif" width="720" alt="Demonstração do ForgetMeNot: a tarefa Marcar a apresentação do TCC é adicionada com urgência alta e prazo 14/11/2026; depois a tarefa Estudar para a prova de Estrutura de Dados é concluída e a barra de progresso avança; por fim uma tarefa concluída é apagada pela janela de confirmação">
</p>

Gravado com o Playwright, com o app rodando localmente (`python src/app.py`) e tarefas de exemplo. A dica do dia vem da Advice Slip API na hora, por isso muda a cada recarga. O app tem só o tema claro.

## Como rodar em 60 segundos

Precisa do Git e do Python 3.11 ou mais novo.

```bash
git clone https://github.com/IsaacGomes260653/forget_me_not.git
cd forget_me_not
python -m venv .venv
source .venv/bin/activate     # no Windows (PowerShell): .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/app.py
```

Abra <http://127.0.0.1:5000>. Num clone limpo, do `git clone` até o app no ar, levou cerca de 30 segundos (Windows 11 e Python 3.12). A CI instala as mesmas dependências no Ubuntu, com Python 3.11.

- Para a versão de terminal, rode `python src/main.py`. As duas versões leem e gravam o mesmo `tasks.json`.
- Rode os comandos na raiz do projeto: o `tasks.json` é procurado na pasta em que você está. O do repositório já vem com cinco tarefas de exemplo.
- Se o PowerShell bloquear o `Activate.ps1`, rode antes `Set-ExecutionPolicy -Scope Process Bypass`, que vale só para aquela janela.

## O que ele faz

Na web (`src/app.py`):

- **Tarefa com urgência e prazo.** Descrição de até 80 caracteres (o contador fica laranja depois de 60), urgência Alta, Média ou Baixa e prazo opcional.
- **Prazo que avisa.** Uma pendente com prazo aparece em vermelho quando venceu ("Vencido em 10/11/2026"), em laranja no dia ("Vence hoje!") e em verde quando ainda há tempo.
- **Pendentes e concluídas separadas**, cada seção com a sua contagem. O cabeçalho mostra a data de hoje e quantas tarefas faltam.
- **Barra de progresso** com "X/Y concluídas" e um aviso quando todas estão feitas.
- **Apagar pede confirmação** numa janela que fecha com Cancelar ou com um clique fora dela.
- **Dica do dia** da [Advice Slip API](https://api.adviceslip.com), em inglês, buscada a cada carregamento da página.
- **Tudo salvo em `tasks.json`**, sem banco de dados.

No terminal (`src/main.py`): um menu com cinco opções (adicionar, listar, concluir, deletar e sair) e a lista numa tabela colorida, feita com o rich. No terminal a tarefa não tem prazo.

<p align="center">
  <img src=".github/capturas/terminal.png" width="640" alt="Versão de terminal: o menu do ForgetMeNot com cinco opções e, depois da opção 2, a tabela com ID, tarefa, urgência colorida e status pendente ou concluída">
</p>

<details>
<summary>No celular</summary>
<br>
<p align="center">
  <img src=".github/capturas/celular.png" width="300" alt="ForgetMeNot numa tela de 390 px: o formulário quebra em duas linhas e as tarefas ocupam a largura toda, com os botões Concluir e Deletar ao lado">
</p>

</details>

