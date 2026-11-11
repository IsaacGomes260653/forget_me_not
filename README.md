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

## Como foi feito

| Escolha | Por quê |
|---|---|
| Python e Flask | A página e as quatro rotas cabem em um arquivo de 73 linhas, sem estrutura obrigatória de projeto. |
| Jinja (`templates/index.html`) | Contagens, barra de progresso e seções já saem prontas do servidor. O JavaScript cuida só do que depende do navegador: a data, a cor do prazo, o contador de caracteres e a janela de confirmação. |
| Arquivo JSON | Dá para abrir e ler, e serve à web e ao terminal ao mesmo tempo. Para o tamanho do projeto, não precisava de banco. |
| Requests | Busca a dica com limite de 5 segundos. |
| rich | Tabela colorida e emojis no terminal, sem escrever códigos de cor na mão. |
| Pytest e `unittest.mock` | Testam a persistência e a dica, com a API de verdade e com a API simulada. |
| Flake8 | Padroniza o código. A CI falha se ele reclamar. |
| GitHub Actions | Roda o lint e os testes em cada push e pull request para a `main`. |
| Gunicorn e Render | O servidor do Flask é só para desenvolvimento. No Render, o app sobe com `gunicorn src.app:app`, do `Procfile`. |

```mermaid
flowchart LR
    N["Navegador"] -->|"GET /"| A["src/app.py<br/>Flask"]
    N -->|"POST /adicionar<br/>GET /concluir/n<br/>GET /deletar/n"| A
    A -->|"render_template"| T["templates/index.html<br/>Jinja e JavaScript"]
    T -->|"página pronta"| N
    A <-->|"lê e grava"| J[("tasks.json")]
    A -->|"requests, até 5 s"| D["Advice Slip API"]
    D -.->|"se falhar: dica fixa"| A
    C["src/main.py<br/>terminal com rich"] <-->|"lê e grava"| J
```

Cada ação (adicionar, concluir ou apagar) carrega o `tasks.json`, muda a lista, grava o arquivo e redireciona para `/`, que monta a página de novo com a lista atualizada e busca outra dica.

<details>
<summary>Estrutura de pastas</summary>

```
.
├── src/
│   ├── app.py            # app web: as rotas do Flask e a dica do dia
│   └── main.py           # versão de terminal: menu e tabela do rich
├── templates/
│   └── index.html        # a página: Jinja, CSS e o JavaScript dos prazos e da confirmação
├── tests/
│   └── test_main.py      # 7 testes: persistência, lógica e a Advice Slip API
├── tasks.json            # as tarefas (vem com cinco de exemplo)
├── requirements.txt      # dependências com versão fixa
├── Procfile              # comando do Render: gunicorn src.app:app
├── VERSION               # 1.0.0
├── .gitattributes        # tira o HTML da contagem de linguagens do GitHub
└── .github/
    ├── workflows/ci.yml  # CI: flake8 e pytest
    └── capturas/         # GIF e capturas deste README
```

</details>

### Decisões técnicas e o que eu aprendi

- **API externa com plano B.** O `buscar_dica()` espera no máximo 5 segundos e, se qualquer coisa der errado, devolve "Foque no que importa: uma tarefa de cada vez." A página nunca quebra por causa da dica, e dois testes com mock cobrem os dois caminhos.
- **Post/Redirect/Get.** Toda ação termina num redirecionamento para `/`. Por isso, recarregar a página depois de adicionar uma tarefa não cria a mesma tarefa de novo.
- **A posição na lista como identificador.** As tarefas não têm id: concluir e apagar usam a posição delas no `tasks.json`. O template percorre a lista inteira, e não uma lista filtrada, para que `loop.index0` continue apontando para a posição certa mesmo com as tarefas divididas em duas seções. Funciona, mas tem limites (veja os próximos passos).
- **O servidor calcula, o navegador cuida do relógio.** As contagens vêm do Jinja; a cor do prazo é calculada no navegador, com a data de quem está olhando. Ao revisar este README, descobri um bug nessa parte: a data de hoje sai do `toISOString()`, que está em UTC, e depois das 21h em Brasília uma tarefa que vence hoje aparece como vencida.
- **Servidor de desenvolvimento não é servidor de produção.** `python src/app.py` usa o servidor do Flask, com debug ligado. No Render, quem atende é o Gunicorn.
- **Teste de integração depende da internet.** Dois testes chamam a Advice Slip API de verdade: provam que a integração funciona, mas derrubam a CI se a API sair do ar. Os testes com mock cobrem a mesma função sem rede.

