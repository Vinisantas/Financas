from collections import defaultdict

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
        if not transacoes or not mes:
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
        return transacoes

    def gerar_resumo_mensal(self, mes: str | None):
        """Gera um resumo de receitas, despesas e saldo para um mês específico."""
        transacoes = self.obter_transacoes()
        if mes:
            transacoes = [t for t in transacoes if t["data"].split("-")[1] == mes]

        receitas = sum(t["valor"] for t in transacoes if t["tipo"] == "r")
        despesas = sum(t["valor"] for t in transacoes if t["tipo"] == "d")
        saldo = receitas - despesas

        return {"receitas": receitas, "despesas": despesas, "saldo": saldo}

    def agrupar_por_categoria(self, mes: str | None):
        """Agrupa as transações por categoria, separando receitas e despesas."""
        transacoes = self.obter_transacoes()
        if mes:
            transacoes = [t for t in transacoes if t["data"].split("-")[1] == mes]

        categorias = {"receitas": defaultdict(float), "despesas": defaultdict(float)}

        for t in transacoes:
            if t["tipo"] == "r":
                categorias["receitas"][t["categoria"]] += t["valor"]
            else:
                categorias["despesas"][t["categoria"]] += t["valor"]

        return {
            "receitas": dict(categorias["receitas"]),
            "despesas": dict(categorias["despesas"]),
        }

    def calcular_evolucao_mensal(self):
        """Calcula a soma de receitas e despesas para cada mês."""
        transacoes = self.obter_transacoes()
        evolucao = defaultdict(lambda: {"receitas": 0.0, "despesas": 0.0})

        for t in transacoes:
            mes = t["data"].split("-")[1]  # Extrai o mês (ex: "01", "02")
            if t["tipo"] == "r":
                evolucao[mes]["receitas"] += t["valor"]
            else:
                evolucao[mes]["despesas"] += t["valor"]

        # Ordena por mês
        sorted_evolucao = sorted(evolucao.items())

        return [
            {"mes": mes, "valores": valores} for mes, valores in sorted_evolucao
        ]