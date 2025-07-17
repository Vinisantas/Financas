class Relatorios:
    def __init__(self, transacao):
        self.transacoes = transacao

    def filtrar_por_categoria(self, categoria):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
            return []

        return [t for t in self.transacoes if t["categoria"] == categoria]

    def filtrar_por_mes(self):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
            return

        mes = input("Qual mês deseja filtrar? (1 a 12): ").zfill(2)
        return self.filtrar_por_mes_api(mes)

    def filtrar_por_mes_api(self, mes):
        return [t for t in self.transacoes if t["data"].split("-")[1] == mes]

    def gerar_relatorio(self):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
            return

        print("\n--- Relatório de Transações ---")
        for t in self.transacoes:
            print(
                f"{t['data']} - {t['tipo'].capitalize()} de R${t['valor']} "
                f"em {t['categoria']} ({t['descricao']})"
            )

    def gerar_relatorio_api(self):
        if not self.transacoes:
            return {"mensagem": "Nenhuma transação registrada."}

        relatorio = []
        for t in self.transacoes:
            relatorio.append(
                {
                    "data": t["data"],
                    "tipo": t["tipo"].capitalize(),
                    "valor": t["valor"],
                    "categoria": t["categoria"],
                    "descricao": t["descricao"],
                }
            )
        return relatorio
