class Financas:
    def __init__(self):
        self.saldo = 0
        self.ganhos = []
        self.despesas = []
        self.transacao = []

    def extrato(self):
        self.atualizar_saldo()
        print(f"Saldo igual a {self.saldo}")
        return self.saldo

    def adicionar_receita(self):
        valor = float(input("Quanto quer adicionar? "))
        self.ganhos.append(valor)
        self.adicionar_transacao("receita", valor)
        self.atualizar_saldo()
        print(f"Adicionado R$ {valor} com sucesso!")
        return valor

    def adicionar_despesa(self):
        valor = float(input("Quanto você retirou? "))
        self.despesas.append(valor)
        self.adicionar_transacao("despesa", valor)
        self.atualizar_saldo()
        print(f"Retirado R$ {valor} com sucesso!")
        return valor

    def atualizar_saldo(self):
        self.saldo = sum(self.ganhos) - sum(self.despesas)

    def adicionar_transacao(self, tipo, valor):
        categoria = input("Categoria: ")
        data = input("Data (dd/mm/aaaa): ")
        descricao = input("Descrição: ")
        transacao = {
            "tipo": tipo,
            "valor": valor,
            "categoria": categoria,
            "data": data,
            "descricao": descricao
        }
        self.transacao.append(transacao)
