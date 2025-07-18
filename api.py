from models.Financas import Financas
from fastapi import FastAPI
from fastapi import Query
from models.schemas import Receita, Despesa
from models.Relatorio import Relatorios
from fastapi.middleware.cors import CORSMiddleware


f = Financas()
app = FastAPI()

# Permitir requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou use ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/saldo")
async def saldo():
    return {"saldo": f.Saldo()}


@app.post("/receita")
async def adicionar_receita(receita: Receita):
    f.adicionar_receita(receita.descricao, receita.valor, receita.categoria)
    return {"mensagem": "Receita adicionada com sucesso!"}


@app.post("/despesa")
async def adicionar_despesa(despesa: Despesa):
    f.adicionar_despesa(despesa.descricao, despesa.valor, despesa.categoria)
    return {"mensagem": "Despesa adicionada com sucesso!"}


@app.get("/transacoes")
async def get_transacoes():
    return {"transacoes": f.listar_todas()}


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
