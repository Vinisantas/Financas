💰 MOOBY - App de Controle Financeiro Pessoal
MOOBY é um projeto pessoal feito em Python com foco no gerenciamento de finanças. Com ele, você pode acompanhar seus ganhos, despesas e o saldo atualizado, de forma simples, organizada e extensível.

https://img.shields.io/badge/Status-Em%2520Desenvolvimento-brightgreen
https://img.shields.io/badge/Python-3.12%252B-blue
https://img.shields.io/badge/FastAPI-0.104.1-green
https://img.shields.io/badge/SQLite-Database-lightgrey

🚀 Funcionalidades Atuais
✅ Registro de ganhos e despesas - Interface web intuitiva
✅ Cálculo automático de saldo - Atualizado em tempo real
✅ Sistema de categorias - Organização por tipo de gasto
✅ Histórico de transações - Visualização completa com datas
✅ API RESTful - Backend em FastAPI com endpoints documentados
✅ Banco de dados SQLite - Armazenamento persistente de dados
✅ Interface web responsiva - Design moderno e acessível
✅ Validação de código - Flake8 + Black via pre-commit

🎯 Objetivos Futuros
🔜 Relatórios por período/categoria - Análises detalhadas
🔜 Filtros avançados - Busca por data, categoria e tipo
🔜 Gráficos e visualizações - Dashboard interativo
🔜 Sistema de metas - Definição de objetivos financeiros
🔜 Exportação de dados - CSV, PDF e Excel
🔜 Autenticação de usuários - Sistema de login seguro
🔜 App móvel - Versão PWA ou React Native

🧪 Como executar
Pré-requisitos
Python 3.12+

Git

Instalação e execução
bash
# Clone o repositório
git clone https://github.com/Vinisantas/finances-back-end.git
cd finances-back-end

# Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.\.venv\Scripts\activate.ps1  # Windows PowerShell

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python -m uvicorn main:app --reload

# Acesse a interface web
# http://localhost:8000
Executando testes
bash
# Instale as dependências de teste
pip install pytest

# Execute os testes
pytest --cov=models
📂 Estrutura do Projeto
text
finances-back-end/
├── models/
│   ├── Financas.py        # Lógica de negócio e acesso ao banco
│   ├── Relatorio.py       # Sistema de relatórios (em desenvolvimento)
│   ├── schemas.py         # Modelos Pydantic para validação
│   └── __init__.py
├── view/
│   ├── index.html         # Interface web principal
│   ├── style.css          # Estilos modernos e responsivos
│   └── script.js          # Lógica front-end e chamadas API
├── database/
│   └── financas.db        # Banco de dados SQLite
├── test/
│   └── test_financas.py   # Testes unitários
├── main.py                # Aplicação FastAPI principal
├── requirements.txt       # Dependências do projeto
├── .pre-commit-config.yaml # Configuração do pre-commit
└── README.md
🛠️ Tecnologias Utilizadas
Backend: Python, FastAPI, SQLite, Pydantic

Frontend: HTML5, CSS3, JavaScript (Vanilla)

Ferramentas: Git, GitHub, Pytest, Flake8, Black

Futuro: Docker, React, JWT Auth, Chart.js

📊 API Endpoints
Método	Endpoint	Descrição
GET	/saldo	Retorna o saldo atual
GET	/transacoes	Lista todas as transações
POST	/receita	Adiciona uma nova receita
POST	/despesa	Adiciona uma nova despesa
🧠 Por que esse projeto?
Este app nasceu como prática de lógica de programação e boas práticas em Python, com o objetivo de evoluir para um sistema completo de finanças pessoais, do terminal à web, com foco em aprendizado real.

👨‍💻 Desenvolvedor
VINIXX - Apaixonado por tecnologia, código limpo e Deus 🙏
Estudante de programação focado em desenvolvimento web, automação e IA.

💡 Contribuições
Este projeto é pessoal, mas ideias são bem-vindas!
Sugestões e melhorias podem ser abertas como issues ou pull requests.

📌 Status do Projeto
🟢 Em desenvolvimento contínuo - Novas funcionalidades sendo adicionadas regularmente

⭐ Dê uma estrela no repositório se este projeto te ajudou ou inspirou!
