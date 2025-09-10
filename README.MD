# MOOBY - App de Controle Financeiro Pessoal

MOOBY é um projeto pessoal feito em Python com foco no gerenciamento de finanças. Com ele, você pode acompanhar seus ganhos, despesas e o saldo atualizado, de forma simples, organizada e extensível.

---

## Funcionalidades Atuais

* Registro de ganhos
* Registro de despesas
* Cálculo automático de saldo
* Estrutura orientada a objetos
* Menu interativo no terminal
* Testes automatizados com `pytest`
* Validação de código com `flake8` + `black` via `pre-commit`
* Estrutura modular com `models`, `views` e `test`

---

## Objetivos Futuros

* Registro completo de transações (categoria, descrição, data)
* Histórico com filtros
* Relatórios por período/categoria (`Relatorio.py`)
* Integração com banco de dados (SQLite / MySQL)
* Containerização com Docker
* CI/CD com GitHub Actions
* Interface Web/Mobile (Flask ou FastAPI + React)
* IA para análises e previsões financeiras

---

## Como executar os testes

```bash
# Instale as dependências
pip install -r requirements.txt

# Rode os testes com cobertura
pytest --cov=models


Estrutura do Projeto
controle-financeiro/
├── models/
│   ├── Financas.py        # Lógica de receitas, despesas, saldo e transações
│   ├── Relatorio.py       # (em desenvolvimento)
│   └── __init__.py
├── views/
│   └── terminal.py        # Interface de terminal com menu interativo
├── test/
│   └── test_financas.py   # Testes unitários com pytest
├── data/
│   └── transacoes.json    # Armazenamento temporário das transações
├── .pre-commit-config.yaml
├── requirements.txt
├── README.md
└── .gitignore

Tecnologias Utilizadas

Python 3.13

Pytest + Coverage

Flake8 + Black + Pre-commit

Git + GitHub

Futuro: Docker • SQLite/MySQL • FastAPI • GitHub Actions • IA com Python

Por que esse projeto?

Este app nasceu como prática de lógica de programação e boas práticas em Python, com o objetivo de evoluir para um sistema completo de finanças pessoais, do terminal à web, com foco em aprendizado real.

Desenvolvedor

VINIXX
Apaixonado por tecnologia, código limpo, academia e Deus
Estudante de programação focado em desenvolvimento web, automação e IA.

Contribuições

Este projeto é pessoal, mas ideias são bem-vindas!
Sugestões e melhorias podem ser abertas como issues ou pull requests.

Status

Em desenvolvimento contínuo
