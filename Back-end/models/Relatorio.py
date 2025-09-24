class Relatorios:
    def __init__(self, transacao):
        self.transacoes = transacao

    def filtrar_por_categoria(self, categoria):
        if not self.transacoes:
            return []
        return [t for t in self.transacoes if t["categoria"] == categoria]

    def filtrar_por_categoria_api(self, categoria):
        return self.filtrar_por_categoria(categoria)

    def filtrar_por_mes(self):
        if not self.transacoes:
            return []
        mes = input("Qual mês deseja filtrar? (1 a 12): ").zfill(2)
        return self.filtrar_por_mes_api(mes)

    def filtrar_por_mes_api(self, mes):
        if not self.transacoes:
            return []
        return [t for t in self.transacoes if t["data"].split("-")[1] == mes]

    def filtrar_por_tipo_api(self, tipo):
        """Filtra por tipo: receita ou despesa"""
        if not self.transacoes:
            return []
        return [t for t in self.transacoes if t["tipo"].lower() == tipo.lower()]

    def soma_por_tipo_api(self, tipo):
        """Soma valores de receita ou despesa"""
        if not self.transacoes:
            return 0
        return sum(
            t["valor"] for t in self.transacoes if t["tipo"].lower() == tipo.lower()
        )

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
        return [
            {
                "data": t["data"],
                "tipo": t["tipo"].capitalize(),
                "valor": t["valor"],
                "categoria": t["categoria"],
                "descricao": t["descricao"],
            }
            for t in self.transacoes
        ]
