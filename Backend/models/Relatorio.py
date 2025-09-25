class Relatorios:
    def __init__(self, financas):
        self.financas = financas  # Recebe a instância de Financas

    def obter_transacoes(self):
        """Obtém todas as transações do banco"""
        return self.financas.listar_todas()

    def filtrar_por_categoria(self, categoria):
        transacoes = self.obter_transacoes()
        if not transacoes:
            return []
        return [t for t in transacoes if t["categoria"] == categoria]

    def filtrar_por_categoria_api(self, categoria):
        return self.filtrar_por_categoria(categoria)

    def filtrar_por_mes_api(self, mes):
        transacoes = self.obter_transacoes()
        if not transacoes:
            return []
        return [t for t in transacoes if t["data"].split("-")[1] == mes]

    def filtrar_por_tipo_api(self, tipo):
        """Filtra por tipo: receita ou despesa"""
        transacoes = self.obter_transacoes()
        if not transacoes:
            return []
        return [t for t in transacoes if t["tipo"].lower() == tipo.lower()]

    def soma_por_tipo_api(self, tipo):
        """Soma valores de receita ou despesa"""
        transacoes = self.obter_transacoes()
        if not transacoes:
            return 0
        return sum(
            t["valor"] for t in transacoes if t["tipo"].lower() == tipo.lower()
        )

    def gerar_relatorio_api(self):
        transacoes = self.obter_transacoes()
        if not transacoes:
            return {"mensagem": "Nenhuma transação registrada."}
        return [
            {
                "data": t["data"],
                "tipo": t["tipo"].capitalize(),
                "valor": t["valor"],
                "categoria": t["categoria"],
                "descricao": t["descricao"],
            }
            for t in transacoes
        ]