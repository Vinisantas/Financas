from fastapi import APIRouter, Query
from models.Financas import Financas
from models.Relatorio import Relatorios


f = Financas()
# Cria um roteador. É ele que vamos importar no main.py
router = APIRouter()

# Rota para relatórios


@router.get("/relatorios/categoria")
async def relatorio_por_categoria(
    categoria: str = Query(..., description="Categoria para filtrar")
):
    relatorios = Relatorios(transacao=f.transacao)
    relatorio = relatorios.filtrar_por_categoria_api(categoria)
    return {"relatorio": relatorio}


@router.get("/relatorios/mes")
async def relatorio_por_mes(
    mes: str = Query(..., description="Mês para filtrar (1-12)")
):
    relatorios = Relatorios(transacao=f.transacao)
    relatorio = relatorios.filtrar_por_mes_api(mes)
    return {"relatorio": relatorio}


@router.get("/relatorios/tipo")
async def relatorio_por_tipo(tipo: str = Query(..., description="(r ou d)")):
    relatorios = Relatorios(transacao=f.transacao)
    relatorio = relatorios.filtrar_por_tipo_api(tipo)
    return {"relatorio": relatorio}


@router.get("/relatorios/soma")
async def relatorio_soma_por_tipo(
    tipo: str = Query(..., description="Tipo para somar (receita ou despesa)")
):
    relatorios = Relatorios(transacao=f.transacao)
    relatorio = relatorios.soma_por_tipo_api(tipo)
    return {"relatorio": relatorio}
