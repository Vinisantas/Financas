import os
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
from dotenv import load_dotenv

# Carrega variáveis do .env (quando rodar localmente)
load_dotenv()

class Financas:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        if not self.DATABASE_URL:
            raise ValueError("❌ DATABASE_URL não encontrada. Defina no Render ou em um arquivo .env")
        self.criar_tabela()

    def conectar(self):
        return psycopg2.connect(self.DATABASE_URL, cursor_factory=RealDictCursor)

    def criar_tabela(self):
        with self.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
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
                conn.commit()

    def adicionar_receita(self, descricao, valor, categoria):
        with self.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO transacao (valor, descricao, categoria, tipo, data)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (valor, descricao, categoria, "r", datetime.now()),
                )
                conn.commit()

    def adicionar_despesa(self, descricao, valor, categoria):
        with self.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO transacao (valor, descricao, categoria, tipo, data)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (valor, descricao, categoria, "d", datetime.now()),
                )
                conn.commit()

    def listar_todas(self):
        with self.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, valor, descricao, categoria, tipo, data FROM transacao ORDER BY data DESC"
                )
                return cursor.fetchall()

    def Saldo(self):
        with self.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT 
                        COALESCE(SUM(CASE WHEN tipo = 'r' THEN valor ELSE 0 END), 0) -
                        COALESCE(SUM(CASE WHEN tipo = 'd' THEN valor ELSE 0 END), 0) 
                        AS saldo
                    FROM transacao
                    """
                )
                return cursor.fetchone()["saldo"]

    def deleta_transacao(self, id):
        with self.conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM transacao WHERE id = %s", (id,)
                )
                conn.commit()
