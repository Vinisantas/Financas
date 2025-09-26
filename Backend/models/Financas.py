import os
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
from dotenv import load_dotenv

# Carrega variáveis do .env (quando rodar localmente)
load_dotenv()

class Financas:
    def __init__(self):
        DATABASE_URL = os.getenv("DATABASE_URL")
        if not DATABASE_URL:
            raise ValueError("❌ DATABASE_URL não encontrada. Defina no Render ou em um arquivo .env")

        # Conexão com PostgreSQL
        self.conn = psycopg2.connect(DATABASE_URL)
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS transacao (
                id SERIAL PRIMARY KEY,
                valor NUMERIC,
                descricao TEXT,
                categoria TEXT,
                tipo CHAR(1),
                data TIMESTAMP
            )
            """
        )
        self.conn.commit()

    def adicionar_receita(self, descricao, valor, categoria):
        self.cursor.execute(
            """
            INSERT INTO transacao (valor, descricao, categoria, tipo, data)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (valor, descricao, categoria, "r", datetime.now()),
        )
        self.conn.commit()

    def adicionar_despesa(self, descricao, valor, categoria):
        self.cursor.execute(
            """
            INSERT INTO transacao (valor, descricao, categoria, tipo, data)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (valor, descricao, categoria, "d", datetime.now()),
        )
        self.conn.commit()

    def listar_todas(self):
        self.cursor.execute(
            "SELECT id, valor, descricao, categoria, tipo, data FROM transacao ORDER BY data DESC"
        )
        return self.cursor.fetchall()

    def Saldo(self):
        self.cursor.execute(
            """
            SELECT 
                COALESCE(SUM(CASE WHEN tipo = 'r' THEN valor ELSE 0 END), 0) -
                COALESCE(SUM(CASE WHEN tipo = 'd' THEN valor ELSE 0 END), 0) 
                AS saldo
            FROM transacao
            """
        )
        return self.cursor.fetchone()["saldo"]

    def deleta_transacao(self, id):
        self.cursor.execute(
            "DELETE FROM transacao WHERE id = %s", (id,)
        )
        self.conn.commit()
