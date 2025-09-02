from models.Financas import Financas
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi import Query
from models.schemas import Receita, Despesa
from models.Relatorio import Relatorios
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import pandas as pd
import io
import os  # Importe o módulo os
import logging

# Configuração de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Inicializa
f = Financas()
app = FastAPI()

# Permite qualquer origem (para testes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Rotas ---
@app.get("/saldo")
async def saldo():
    return {"saldo": f.Saldo()}

@app.post("/receita")
async def adicionar_receita(receita: Receita):
    f.adicionar_receita(receita.descricao, receita.valor, receita.categoria)
    return {"mensagem": "Receita adicionada com sucesso!", "transacoes": f.listar_todas()}

@app.post("/despesa")
async def adicionar_despesa(despesa: Despesa):
    f.adicionar_despesa(despesa.descricao, despesa.valor, despesa.categoria)
    return {"mensagem": "Despesa adicionada com sucesso!", "transacoes": f.listar_todas()}

@app.get("/transacoes")
async def get_transacoes():
    return {"transacoes": f.listar_todas()}

@app.post("/adiciona_csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="O arquivo deve ser um CSV")
    try:
        contents = await file.read()
        temp_file_path = f"temp_{file.filename}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(contents)

        f.processar_extrato_nubank(temp_file_path)
        os.remove(temp_file_path)

        # Retorna as transações atualizadas diretamente
        return {
            "filename": file.filename,
            "message": "Extrato processado com sucesso!",
            "transacoes": f.listar_todas()
        }
    except Exception as e:
        logging.error(f"Erro ao processar o CSV: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Erro ao processar o CSV: {e}")
    














@app.get("/relatorios/categoria")
async def relatorio_por_categoria(
    categoria: str = Query(..., description="Categoria para filtrar")
):
    relatorios = Relatorios(transacao=f.transacao)
    relatorio = relatorios.filtrar_por_categoria_api(categoria)
    return {"relatorio": relatorio}


@app.get("/relatorios/mes")
async def relatorio_por_mes(
    mes: str = Query(..., description="Mês para filtrar (1-12)")
):
    relatorios = Relatorios(transacao=f.transacao)
    relatorio = relatorios.filtrar_por_mes_api(mes)
    return {"relatorio": relatorio}


@app.get("/relatorios/tipo")
async def relatorio_por_tipo(tipo: str = Query(..., description="(r ou d)")):
    relatorios = Relatorios(transacao=f.transacao)
    relatorio = relatorios.filtrar_por_tipo_api(tipo)
    return {"relatorio": relatorio}


@app.get("/relatorios/soma")
async def relatorio_soma_por_tipo(
    tipo: str = Query(..., description="Tipo para somar (receita ou despesa)")
):
    relatorios = Relatorios(transacao=f.transacao)
    relatorio = relatorios.soma_por_tipo_api(tipo)
    return {"relatorio": relatorio}
