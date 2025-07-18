from pydantic import BaseModel


class Receita(BaseModel):
    valor: float
    descricao: str
    categoria: str


class Despesa(BaseModel):
    valor: float
    descricao: str
    categoria: str
