

import json

def carregar_dados():
    try:
        with open("transacao.json", 'r') as arquivo:
            return json.load(arquivo)
        arquivo.close()
    except FileNotFoundError:
        return []
    

def salvar_dados(dados):
    try:
        with open("transacao.json", 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
        arquivo.close()
    except FileNotFoundError:
        return []