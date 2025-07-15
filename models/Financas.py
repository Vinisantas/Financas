import datetime
from utils.arquivos import carregar_dados, salvar_dados


class Financas:
    def __init__(self):
        self.saldo = 0
        self.ganhos = []
        self.despesas = []
        self.transacao = carregar_dados()  # carrega dados em formato json

    def extrato(self):
        self.atualizar_saldo()
        print(f"Saldo igual a {self.saldo}  ")
        print("------------------------------------------")
        return self.saldo

    def adicionar_receita(self, valor, categoria, descricao):
        self.ganhos.append(valor)
        self.adicionar_transacao("receita", valor, categoria, descricao)
        self.atualizar_saldo()
        print(f"Adicionado R$ {valor} com sucesso!")
        return valor

    def adicionar_despesa(self, valor, categoria, descricao):
        self.despesas.append(valor)
        self.adicionar_transacao("despesa", valor, categoria, descricao)
        self.atualizar_saldo()
        print(f"Retirado R$ {valor} com sucesso!")
        return valor

    def atualizar_saldo(self):
        self.saldo = sum(self.ganhos) - sum(self.despesas)

    def adicionar_transacao(self, tipo, valor, categoria, descricao):
        data = self.get_day_format()
        transacao = {
            "tipo": tipo,
            "valor": valor,
            "categoria": categoria,
            "data": data,
            "descricao": descricao,
        }
        self.transacao.append(transacao)
        salvar_dados(self.transacao)
        print("Transação adicionada com sucesso!")

    @staticmethod
    def get_day_format():
        now = datetime.datetime.now()
        today = now.strftime("%d-%m-%Y %H:%M:%S")
        return today
