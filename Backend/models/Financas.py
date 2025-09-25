import sqlite3
from datetime import datetime


class Financas:
    def __init__(self):
        self.conn = sqlite3.connect("database/financas.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS transacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL,
                descricao TEXT,
                categoria TEXT,
                tipo TEXT,
                data TEXT
            )
        """
        )
        self.conn.commit()

    def adicionar_receita(self, descricao, valor, categoria):
        self.cursor.execute(
            "INSERT INTO transacao (valor, descricao, categoria, tipo, data) VALUES (?, ?, ?, ?, ?)",
            (
                valor,
                descricao,
                categoria,
                "r",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ),
        )
        self.conn.commit()

    def adicionar_despesa(self, descricao, valor, categoria):
        self.cursor.execute(
            "INSERT INTO transacao (valor, descricao,  categoria, tipo, data) VALUES (?, ?, ?, ?, ?)",
            (
                valor,
                descricao,
                categoria,
                "d",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ),
        )
        self.conn.commit()

    def listar_todas(self):
        self.cursor.execute(
            "SELECT id, valor, descricao, categoria, tipo, data FROM transacao ORDER BY datetime(data) DESC"
        )
        rows = self.cursor.fetchall()
        transacoes = []
        for row in rows:
            transacoes.append({
                "id": row[0],
                "valor": row[1],
                "descricao": row[2],
                "categoria": row[3],
                "tipo": row[4],
                "data": row[5]
            })
        return transacoes


    def Saldo(self):
        self.cursor.execute(
            "SELECT SUM(CASE WHEN tipo='r' THEN valor ELSE 0 END) - SUM(CASE WHEN tipo='d' THEN valor ELSE 0 END) FROM transacao"
        )
        saldo = self.cursor.fetchone()[0]
        return saldo

    def deleta_transacao(self, id):
        id_transacao = id
        self.cursor.execute(
            "DELETE FROM transacao WHERE id = ?", (id_transacao,)
        )
        self.conn.commit()
