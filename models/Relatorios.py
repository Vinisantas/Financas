
class Relatorios:
    def __init__(self, transacao):
        self.transacoes = transacao


    def filtrar_por_categoria(self):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
            return
        else:
            categoria = input("Qual categoria quer saber? ")
            for t in self.transacoes:
                if t["categoria"] == categoria:
                    print(f"Dia: {t['data']} | Tipo: {t['tipo']} | Valor: R$ {t['valor']} | Descrição: {t['descricao']}")
                else:
                    print("Nenhuma transação encontrada para essa categoria.")

    def filtrar_por_mes(self):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
            return
        else:
            mes = int(input("Qual mês quer saber? "))
            if mes == 7 :
                print("julho")

    def filtar_por_tipo(self):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
            return
        else:
            tipo = input("Qual tipo deseja filtrar? (receita ou despesa): ").lower()
            resultados = [t for t in self.transacoes if t["tipo"].lower() == tipo]
            if resultados:
                print(f"\nTransações do tipo '{tipo}':\n")
                for t in resultados:
                    print(f"Dia: {t['data']} | Valor: R$ {t['valor']} | Categoria: {t['categoria']} | Descrição: {t['descricao']}")
            else:
                print(f"Nenhuma transação do tipo '{tipo}' encontrada.")