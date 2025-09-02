import sqlite3
import pandas as pd
from datetime import datetime

class Financas:
    def __init__(self):
        self.conn = sqlite3.connect("data/financas.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT,
                valor REAL,
                categoria TEXT,
                tipo TEXT,
                data TEXT
            )
        """)
        self.conn.commit()

    def adicionar_receita(self, descricao, valor, categoria):
        self.cursor.execute(
            "INSERT INTO transacao (descricao, valor, categoria, tipo, data) VALUES (?, ?, ?, ?, ?)",
            (descricao, valor, categoria, 'r', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        )
        self.conn.commit()

    def adicionar_despesa(self, descricao, valor, categoria):
        self.cursor.execute(
            "INSERT INTO transacao (descricao, valor, categoria, tipo, data) VALUES (?, ?, ?, ?, ?)",
            (descricao, valor, categoria, 'd', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        )
        self.conn.commit()

    def listar_todas(self):
        self.cursor.execute("SELECT  valor, categoria, tipo, data FROM transacao ORDER BY datetime(data) DESC")
        rows = self.cursor.fetchall()
        transacoes = []
        for row in rows:
            transacoes.append({
                "valor": row[0],
                "categoria": row[1],
                "tipo": row[2],
                "data": row[3]
            })
        return transacoes

    #despesas esta com sinal negativo então somente somar ela já ajusta o valor
    def Saldo(self):
        self.cursor.execute("SELECT SUM(valor) FROM transacao")
        total = self.cursor.fetchone()[0] or 0
        return total
    
    

    def determinar_tipo_transacao(self, valor):
        valor_num = float(valor)
        return "r" if valor_num > 0 else "d"

    def processar_extrato_nubank(self, caminho_csv):
        df = pd.read_csv(caminho_csv, sep=';')
        for _, row in df.iterrows():
            descricao = str(row['Descrição'])
            valor_str = str(row.get('Valor', '0')).replace('.', '').replace(',', '.')
            try:
                valor = float(valor_str)
            except ValueError:
                valor = 0.0
            categoria = str(row['Categoria'])
            tipo = self.determinar_tipo_transacao(valor)
            data = row.get('data', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            self.cursor.execute(
                "INSERT INTO transacao (descricao, valor, categoria, tipo, data) VALUES (?, ?, ?, ?, ?)",
                (descricao, valor, categoria, tipo, data)
            )
        self.conn.commit()
