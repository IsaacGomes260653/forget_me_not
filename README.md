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

