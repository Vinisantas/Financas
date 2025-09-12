# MOOBY – App de Controle Financeiro Pessoal

[![Status – Em Desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-brightgreen)](https://github.com/Vinisantas/finances-back-end)  
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue)]  
[![FastAPI 0.104.1](https://img.shields.io/badge/FastAPI-0.104.1-green)]  
[![SQLite Database](https://img.shields.io/badge/SQLite-Database-lightgrey)]  

Uma aplicação pessoal desenvolvida com Python e FastAPI para gerenciar suas finanças de forma simples, eficiente e responsiva.

---

##  Funcionalidades Atuais

- ✅ Registro de ganhos e despesas com interface web moderna  
- ✅ Cálculo de saldo em tempo real  
- ✅ Organização de transações por categoria  
- ✅ Histórico completo com datas  
- ✅ Backend em FastAPI com API RESTful documentada  
- ✅ Banco de dados persistente via SQLite  
- ✅ Frontend responsivo usando HTML5, CSS3 e JavaScript Vanilla  
- ✅ Validação e formatação de código com Flake8 + Black e pre-commit

---

##  Objetivos Futuros

- Relatórios detalhados por período ou categoria  
- Filtros avançados: data, categoria, tipo de transação  
- Dashboard com gráficos interativos  
- Sistema de metas financeiras  
- Exportação de dados em CSV, PDF ou Excel  
- Autenticação segura (login de usuários via JWT)  
- Aplicativo móvel (PWA ou React Native)

---

##  Como Executar

### Pré-requisitos

- Python 3.12+  
- Git

### Passos

```bash
# Clonar o repositório
git clone https://github.com/Vinisantas/finances-back-end.git
cd finances-back-end

# Criar e ativar um ambiente virtual
python -m venv .venv
source .venv/bin/activate     # Linux/Mac
# ou
.\.venv\Scripts\activate.ps1  # Windows PowerShell

# Instalar dependências
pip install -r requirements.txt

# Executar a aplicação
python -m uvicorn main:app --reload

# Acesse no navegador:
http://localhost:8000

Executar Testes
# Instalar Pytest (caso ainda não tenha)
pip install pytest

# Rodar testes com cobertura
pytest --cov=models

Estrutura do Projeto
finances-back-end/
├── models/
│   ├── Financas.py     # Lógica de negócio e acesso ao banco
│   ├── Relatorio.py    # Módulo de relatórios (em desenvolvimento)
│   ├── schemas.py      # Modelos Pydantic para validação
│   └── __init__.py
├── view/
│   ├── index.html      # Interface web principal
│   ├── style.css       # Estilos modernos e responsivos
│   └── script.js       # Lógica front-end e chamadas à API
├── database/
│   └── financas.db     # Banco de dados SQLite
├── test/
│   └── test_financas.py # Testes unitários
├── main.py              # Versão principal do FastAPI app
├── requirements.txt     # Dependências do projeto
├── .pre-commit-config.yaml
└── README.md

Tecnologias Utilizadas

Backend: Python • FastAPI • SQLite • Pydantic

Frontend: HTML5 • CSS3 • JavaScript (Vanilla)

Ferramentas: Git • GitHub • Pytest • Flake8 • Black • pre-commit

Planejado para o futuro: Docker • React • JWT Auth • Chart.js

Endpoints da API
Método	Rota	Descrição
GET	/saldo	Retorna o saldo atual
GET	/transacoes	Lista todas as transações
POST	/receita	Adiciona uma nova receita
POST	/despesa	Adiciona uma nova despesa
Por que este projeto?

Esse app é um exercício prático de lógica, organização e padrões de código limpo em Python,
com o objetivo de evoluir de uma ferramenta de terminal para um sistema web completo.
