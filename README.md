# API de Finanças Pessoais
# Mooby Finance - Gerenciador Financeiro Pessoal

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.3-05998b.svg)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

Uma API RESTful simples e eficiente para gerenciamento de finanças pessoais, construída com Python e FastAPI.
**Mooby Finance** é uma aplicação web full-stack para gerenciamento de finanças pessoais. Com uma interface moderna e intuitiva e um back-end robusto, permite que o usuário registre receitas e despesas, consulte o saldo e gere relatórios detalhados sobre sua vida financeira.

## 📋 Sobre o Projeto

<img width="1829" height="876" alt="image" src="https://github.com/user-attachments/assets/6314dbf0-b6c3-468a-b3b9-f9c05c6b055b" />
<img width="1840" height="702" alt="image" src="https://github.com/user-attachments/assets/4f398d10-3537-491d-9a75-dcd8161a8bda" />
<img width="1668" height="692" alt="image" src="https://github.com/user-attachments/assets/e5eea7e5-75e5-4f5a-b778-9bc5ae3f3d10" />





Este projeto é dividido em duas partes principais:
-   **Back-end**: Uma API RESTful construída com Python e FastAPI, responsável por toda a lógica de negócio, processamento e armazenamento (em memória) das transações.
-   **Front-end**: Uma interface de usuário reativa construída com HTML, CSS e JavaScript puros, que consome a API do back-end para fornecer uma experiência visualmente agradável e funcional.

## ✨ Arquitetura do Projeto

Este projeto fornece uma API para registrar, consultar e gerenciar transações financeiras, como receitas e despesas. Ele também oferece endpoints para a geração de relatórios básicos, permitindo uma análise rápida das suas finanças.
A aplicação segue uma arquitetura cliente-servidor clássica:

1.  **Front-end (Cliente)**: O usuário interage com as páginas HTML (`index.html`, `financas.html`, `relatorios.html`). As ações (como adicionar uma despesa) são capturadas por JavaScript.
2.  **Comunicação (HTTP)**: O JavaScript realiza chamadas (`fetch`) para a API do back-end, enviando e recebendo dados no formato JSON.
3.  **Back-end (Servidor)**: O servidor FastAPI recebe as requisições, processa os dados usando as classes de modelo (`Financas`, `Relatorios`), e retorna a resposta apropriada para o front-end.

## ✨ Funcionalidades

-   **Consulta de Saldo**: Verifique o saldo atual (total de receitas - total de despesas).
-   **Listagem de Transações**: Visualize todas as transações registradas.
-   **Exclusão de Transações**: Remova uma transação específica pelo seu ID.
-   **Relatórios**: Gere relatórios filtrando transações por categoria, mês ou tipo.
-   **Relatórios Detalhados**:
    -   Resumo mensal (saldo, total de receitas, total de despesas).
    -   Gráficos de distribuição de gastos e receitas por categoria.
    -   Visualização da evolução financeira ao longo dos meses.

## 🛠️ Tecnologias Utilizadas

-   **Python**: Linguagem de programação principal.
-   **FastAPI**: Framework web para a construção da API.
-   **Uvicorn**: Servidor ASGI para rodar a aplicação.
-   **Pydantic**: Para validação e serialização de dados.

### Back-end
-   **Python**: Linguagem de programação.
-   **FastAPI**: Framework web de alta performance para a construção da API.
-   **Uvicorn**: Servidor ASGI para executar a aplicação FastAPI.
-   **Pydantic**: Para validação e configuração de dados.

### Front-end
-   **HTML5**: Estrutura das páginas web.
-   **CSS3**: Estilização, com um design moderno (dark mode) e responsivo.
-   **JavaScript**: Manipulação do DOM, interatividade e comunicação com a API.

## 📂 Estrutura de Arquivos

```
Financas/
├── Back-end/
│   ├── controllers/      # Módulos com os endpoints da API (rotas)
│   ├── models/           # Classes de negócio (Financas, Relatorios)
│   ├── main.py           # Ponto de entrada da aplicação FastAPI
│   └── requirements.txt  # Dependências do Python
│
└── Front-end/
    ├── view/             # Arquivos visíveis para o usuário
    │   ├── index.html
    │   ├── financas.html
    │   ├── relatorios.html
    │   └── style.css
    └── js/               # Arquivos JavaScript (script.js, relatorios.js)
```

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

**1. Clone o repositório:**
### 1. Configurar e Rodar o Back-end

Primeiro, inicie o servidor da API.

```bash
# Clone o repositório (se ainda não o fez)
git clone https://github.com/seu-usuario/Financas.git
cd Financas/Back-end

# Crie e ative um ambiente virtual
# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Inicie o servidor
uvicorn main:app --reload
```

O servidor da API estará rodando em `http://127.0.0.1:8000`. Você pode acessar a documentação interativa em `http://127.0.0.1:8000/docs`.

### 2. Abrir o Front-end

Com o back-end rodando, basta abrir os arquivos HTML no seu navegador.

```bash
git clone https://github.com/Vinisantas/Financas.git


**2. Crie e ative um ambiente virtual:**


# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate

**3. Instale as dependências:**

O arquivo requirements.txt contém todas as bibliotecas necessárias.


pip install -r requirements.txt

**4. Inicie o servidor:**

uvicorn main:app --reload
# Navegue até a pasta do front-end
cd ../Front-end/view
