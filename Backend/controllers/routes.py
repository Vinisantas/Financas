from models.Financas import Financas
from fastapi import APIRouter
from models.schemas import Receita, Despesa

# Inicializa
f = Financas()
# Cria um roteador. É ele que vamos importar no main.py
router = APIRouter()

# --- Rotas ---
@router.get("/saldo")
async def saldo():
    return {"saldo": f.Saldo()}


@router.post("/receita")
async def adicionar_receita(receita: Receita):
    f.adicionar_receita(receita.descricao, receita.valor, receita.categoria)
    return {
        "mensagem": "Receita adicionada com sucesso!",
        "transacoes": f.listar_todas(),
    }


@router.post("/despesa")
async def adicionar_despesa(despesa: Despesa):
    f.adicionar_despesa(despesa.descricao, despesa.valor, despesa.categoria)
    return {
        "mensagem": "Despesa adicionada com sucesso!",
        "transacoes": f.listar_todas(),
    }


@router.get("/transacoes")
async def get_transacoes():
    return {"transacoes": f.listar_todas()}



@router.delete("/deleta/{id}")
async def deleta_transacao(id: int):
    f.deleta_transacao(id)
    return{
        "mensagem": "Transação deletada com sucesso!",
        "transacoes": f.listar_todas(),
    }