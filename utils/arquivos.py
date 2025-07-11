import json
import os

CAMINHO_ARQUIVO = "data/transacoes.json"


def carregar_dados():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r") as f:
            return json.load(f)
    else:
        return []


def salvar_dados(transacoes):
    with open(CAMINHO_ARQUIVO, "w") as f:
        json.dump(transacoes, f, indent=4)
