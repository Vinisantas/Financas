from pydantic import BaseModel


class Receita(BaseModel):
    valor: float
    categoria: str
    descricao: str


class Despesa(BaseModel):
    valor: float
    categoria: str
    descricao: str
