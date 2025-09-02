from datetime import datetime
import sqlite3
import csv  # Importa a biblioteca csv


class Financas:
    def __init__(self):
        # Conecta ao banco ou cria um arquivo chamado financas.db
        self.conn = sqlite3.connect("data/financas.db")
        self.cursor = self.conn.cursor()
        self._criar_tabela()  # Cria a tabela se ela não existir
        self.ganhos = []
        self.despesas = []

    def _criar_tabela(self):
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS transacao (
        id INTEGER PRIMARY KEY,
        tipo TEXT NOT NULL,
        valor REAL,
        categoria TEXT NOT NULL,
        descricao TEXT NOT NULL,
        data TEXT NOT NULL
        )
"""
        )
        self.conn.commit()

    def adicionar_receita(self, descricao, valor, categoria, data):
        #data = datetime.now().strftime("%d-%m-%Y")  # Pega a data atual
        self.cursor.execute(
            """
            INSERT INTO transacao (tipo, valor, categoria, descricao, data)
            VALUES (?, ?, ?, ?, ?)
        """,
            ("r", valor, categoria, descricao, data),
        )
        self.conn.commit()
        self.ganhos.append(
            {
                "tipo": "r",
                "valor": valor,
                "categoria": categoria,
                "descricao": descricao,
                "data": data,
            }
        )

    def adicionar_despesa(self, descricao, valor, categoria, data):
        #data = datetime.now().strftime("%d-%m-%Y")  # Pega a data atual
        self.cursor.execute(
            """
            INSERT INTO transacao (tipo, valor, categoria, descricao, data)
            VALUES (?, ?, ?, ?, ?)
        """,
            ("d", valor, categoria, descricao, data),
        )
        self.conn.commit()
        self.despesas.append(
            {
                "tipo": "d",
                "valor": valor,
                "categoria": categoria,
                "descricao": descricao,
                "data": data,
            }
        )

    def Saldo(self, saldo=0):
        self.listar_todas()
        for transacao in self.ganhos:
            saldo += transacao["valor"]
        for transacao in self.despesas:
            saldo -= transacao["valor"]
        return saldo

    def listar_todas(self):
        self.ganhos = []
        self.despesas = []
        self.cursor.execute("SELECT * FROM transacao WHERE tipo = 'r'")
        for linha in self.cursor.fetchall():
            self.ganhos.append(
                {
                    "tipo": linha[1],
                    "valor": linha[2],
                    "categoria": linha[3],
                    "descricao": linha[4],
                    "data": linha[5],
                }
            )
        self.cursor.execute("SELECT * FROM transacao WHERE tipo = 'd'")
        for linha in self.cursor.fetchall():
            self.despesas.append(
                {
                    "tipo": linha[1],
                    "valor": linha[2],
                    "categoria": linha[3],
                    "descricao": linha[4],
                    "data": linha[5],
                }
            )
        return self.ganhos + self.despesas

    def fechar(self):
        self.conn.close()


    def categorizar_transacao(self, descricao):
        # Aqui você pode usar regras ou ML para determinar a categoria
        # Por enquanto, vamos usar uma lógica simples de exemplo
        descricao_lower = descricao.lower()
        if "mercado" in descricao_lower:
            return "Alimentação"
        elif "Abastecedora" in descricao_lower or "Wingert" in descricao_lower:
            return "Transporte"
        elif "restaurante" in descricao_lower:
            return "Lazer"
        elif "UNINTER" in descricao_lower:
            return "Faculdade"
        else:
            return "Outros"

    def determinar_tipo_transacao(self, descricao, valor):
        # Aqui você pode usar regras ou ML para determinar se é receita ou despesa
        # Por enquanto, vamos usar uma lógica simples de exemplo
        descricao_lower = descricao.lower()
        if valor < 0:
            return "d"
        if "transferência recebida" in descricao_lower or "recebido por pix" in descricao_lower or "transferência Recebida" in descricao_lower:
            return "r"
        else:
            return "d"

    def processar_extrato_nubank(self, arquivo_csv):
        try:
            with open(arquivo_csv, 'r', encoding='utf-8') as arquivo:
                leitor_csv = csv.DictReader(arquivo)
                for linha in leitor_csv:
                    # Garante que a coluna exista
                    data = linha.get('Data')
                    descricao = linha.get('Descrição') or linha.get('descricao') or ''
                    valor_str = linha.get('Valor') or linha.get('valor') or '0'

                    # Converte valor
                    try:
                        valor = float(valor_str.replace(',', '.'))
                    except:
                        valor = 0.0

                    # Se não houver descrição, ignora a linha
                    if not descricao:
                        continue

                    categoria = self.categorizar_transacao(descricao)
                    tipo = self.determinar_tipo_transacao(descricao, valor)


                    if tipo == 'r':
                        self.adicionar_receita(descricao, valor, categoria, data)
                    elif tipo == 'd':
                        self.adicionar_despesa(descricao, valor, categoria, data)

            print("Extrato  processado com sucesso!")

        except FileNotFoundError:
            print(f"Erro: Arquivo não encontrado: {arquivo_csv}")
        except Exception as e:
            print(f"Erro ao processar o extrato: {e}")

