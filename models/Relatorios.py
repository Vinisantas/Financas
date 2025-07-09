

class Relatorios:
    def __init__(self, transacoes):
        self.transacoes = transacoes


    def filtrar_por_categoria(self, categoria):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
            return
        else:
            for i in self.transacoes:
                if i["categoria"] == categoria:
                    print(categoria)