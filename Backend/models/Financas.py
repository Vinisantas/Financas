import os
import psycopg2
from psycopg2 import pool
from psycopg2.extras import RealDictCursor
from datetime import datetime
import pytz
from dotenv import load_dotenv

# Carrega variáveis do .env (quando rodar localmente)
load_dotenv()

class Financas:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        if not self.DATABASE_URL:
            raise ValueError("❌ DATABASE_URL não encontrada. Defina no Render ou em um arquivo .env")
        # Cria um pool de conexões com até 10 conexões simultâneas
        self.pool = psycopg2.pool.SimpleConnectionPool(
            1, 10, self.DATABASE_URL, cursor_factory=RealDictCursor
        )
        self.criar_tabela()

    def conectar(self):
        return self.pool.getconn()

    def liberar(self, conn):
        self.pool.putconn(conn)

    def criar_tabela(self):
        conn = self.conectar()
        try:
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
        finally:
            self.liberar(conn)

    def adicionar_receita(self, descricao, valor, categoria):
        conn = self.conectar()
        try:
            with conn.cursor() as cursor:
                fuso_brasilia = pytz.timezone("America/Sao_Paulo")
                agora = datetime.now(fuso_brasilia)
                data_formatada = agora.strftime("%d/%m/%Y às %H:%M")
                cursor.execute(
                    """
                    INSERT INTO transacao (valor, descricao, categoria, tipo, data)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (valor, descricao, categoria, "r", data_formatada),
                )
                conn.commit()
        finally:
            self.liberar(conn)

    def adicionar_despesa(self, descricao, valor, categoria):
        conn = self.conectar()
        try:
            with conn.cursor() as cursor:
                fuso_brasilia = pytz.timezone("America/Sao_Paulo")
                agora = datetime.now(fuso_brasilia)
                data_formatada = agora.strftime("%d/%m/%Y às %H:%M")
                cursor.execute(
                    """
                    INSERT INTO transacao (valor, descricao, categoria, tipo, data)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (valor, descricao, categoria, "d", data_formatada),
                )
                conn.commit()
        finally:
            self.liberar(conn)

    def listar_todas(self):
        conn = self.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, valor, descricao, categoria, tipo, data FROM transacao ORDER BY data DESC"
                )
                return cursor.fetchall()
        finally:
            self.liberar(conn)

    def Saldo(self):
        conn = self.conectar()
        try:
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
        finally:
            self.liberar(conn)

    def deleta_transacao(self, id):
        conn = self.conectar()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM transacao WHERE id = %s", (id,)
                )
                conn.commit()
        finally:
            self.liberar(conn)
