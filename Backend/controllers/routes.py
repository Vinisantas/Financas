from models.Financas import Financas
from models.Relatorio import Relatorios
from fastapi import APIRouter, Query
from models.schemas import Receita, Despesa
from typing import Optional

# Inicializa
f = Financas()
r = Relatorios(f) # Instancia a classe de Relatórios
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

# --- Rotas de Relatórios ---
@router.get("/relatorio/resumo")
async def get_relatorio_resumo(mes: Optional[str] = Query(None)):
    """Gera um resumo de receitas, despesas e saldo para um dado mês."""
    return r.gerar_resumo_mensal(mes)

@router.get("/relatorio/categorias")
async def get_relatorio_categorias(mes: Optional[str] = Query(None)):
    """Agrupa transações por categoria para um dado mês."""
    return r.agrupar_por_categoria(mes)

@router.get("/relatorio/evolucao")
async def get_relatorio_evolucao():
    """Retorna a evolução de receitas e despesas ao longo dos meses."""
    return r.calcular_evolucao_mensal()

@router.get("/relatorio/transacoes_mes")
async def get_transacoes_mes(mes: Optional[str] = Query(None)):
    """Lista as transações de um mês específico."""
    return r.filtrar_por_mes_api(mes)