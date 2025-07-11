class Relatorios:
    def __init__(self, transacao):
        self.transacoes = transacao

    def filtrar_por_categoria(self):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
            return

        categoria = input("Qual categoria quer saber? ")
        encontrou = False

        for t in self.transacoes:
            if t["categoria"] == categoria:
                # Ajuste para quebrar a linha longa
                print(
                    f"Dia: {t['data']} | Tipo: {t['tipo']} | "
                    f"Valor: R$ {t['valor']:.2f} | "
                    f"Descrição: {t['descricao']}"
                )
                print("------------------------------------------")
                encontrou = True

        if not encontrou:
            print("Nenhuma transação encontrada para essa categoria.")

    def filtrar_por_mes(self):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
            return

        mes = input("Qual mês deseja filtrar? (1 a 12): ").zfill(2)
        resultados = [
            t for t in self.transacoes if t["data"].split("-")[1] == mes
        ]  # noqa: E501

        if resultados:
            print(f"\nTransações do mês '{mes}':\n")
            for t in resultados:
                # Ajuste para quebrar a linha longa
                print(
                    f"Dia: {t['data']} | Valor: R$ {t['valor']:.2f} | "
                    f"Categoria: {t['categoria']} | "
                    f"Descrição: {t['descricao']}"
                )
                print("------------------------------------------")
        else:
            print(f"Nenhuma transação do mês '{mes}' encontrada.")

    def filtrar_por_tipo(self):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
            return

        tipo = input(
            "Qual tipo deseja filtrar? (receita ou despesa): "
        ).lower()  # noqa: E501
        resultados = [t for t in self.transacoes if t["tipo"].lower() == tipo]

        if resultados:
            print(f"\nTransações do tipo '{tipo}':\n")
            for t in resultados:
                # Ajuste para quebrar a linha longa
                print(
                    f"Dia: {t['data']} | Valor: R$ {t['valor']:.2f} | "
                    f"Categoria: {t['categoria']} | "
                    f"Descrição: {t['descricao']}"
                )
                print("------------------------------------------")
        else:
            print(f"Nenhuma transação do tipo '{tipo}' encontrada.")

    def soma_por_tipo(self):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
            return

        tipo = input("Qual tipo deseja somar? (receita ou despesa): ").lower()
        resultados = [t for t in self.transacoes if t["tipo"].lower() == tipo]

        if resultados:
            soma = sum(t["valor"] for t in resultados)
            print(f"Soma dos valores do tipo '{tipo}': R$ {soma:.2f}")
        else:
            print(f"Nenhuma transação do tipo '{tipo}' encontrada.")
