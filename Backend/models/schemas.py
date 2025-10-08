from decimal import Decimal
from pydantic import BaseModel


class Receita(BaseModel):
    valor: Decimal
    descricao: str
    categoria: str


class Despesa(BaseModel):
    valor: Decimal
    descricao: str
    categoria: str
