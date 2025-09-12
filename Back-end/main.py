# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

# Importa o objeto router do seu arquivo de rotas
from controllers.routes import router

# Configuração de logs
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

# Adiciona o middleware CORS à aplicação principal
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui todas as rotas definidas no router na sua aplicação
app.include_router(router)
