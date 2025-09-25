from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

# Importa os objetos router dos seus arquivos de rotas
from controllers.routes import router as transacoes_router
from controllers.routesRelatories import router as relatorios_router

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

# Inclui todas as rotas definidas nos routers na sua aplicação
app.include_router(transacoes_router)
app.include_router(relatorios_router, prefix="/relatorios")

@app.get("/")
def read_root():
    return {"message": "API Financeira funcionando!"}