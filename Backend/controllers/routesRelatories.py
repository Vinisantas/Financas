from fastapi import APIRouter, Query
from models.Financas import Financas
from models.Relatorio import Relatorios

# Cria uma instância global
f = Financas()

router = APIRouter()

@router.get("/categoria")
async def relatorio_por_categoria(
    categoria: str = Query(..., description="Categoria para filtrar")
):
    relatorios = Relatorios(financas=f)  # Passa a instância de Financas
    relatorio = relatorios.filtrar_por_categoria_api(categoria)
    return {"relatorio": relatorio}

@router.get("/mes")
async def relatorio_por_mes(
    mes: str = Query(..., description="Mês para filtrar (1-12)")
):
    relatorios = Relatorios(financas=f)
    relatorio = relatorios.filtrar_por_mes_api(mes)
    return {"relatorio": relatorio}

@router.get("/tipo")
async def relatorio_por_tipo(tipo: str = Query(..., description="(r ou d)")):
    relatorios = Relatorios(financas=f)
    relatorio = relatorios.filtrar_por_tipo_api(tipo)
    return {"relatorio": relatorio}

@router.get("/soma")
async def relatorio_soma_por_tipo(
    tipo: str = Query(..., description="Tipo para somar (receita ou despesa)")
):
    relatorios = Relatorios(financas=f)
    relatorio = relatorios.soma_por_tipo_api(tipo)
    return {"relatorio": relatorio}

@router.get("/todas")
async def relatorio_completo():
    relatorios = Relatorios(financas=f)
    relatorio = relatorios.gerar_relatorio_api()
    return {"relatorio": relatorio}