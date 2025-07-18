import sqlite3  # Importa o módulo para usar SQLite
from datetime import datetime  # Para pegar a data atual


class Financas:
    def __init__(self):
        # Conecta ao banco ou cria um arquivo chamado financas.db
        self.conn = sqlite3.connect("data/financas.db")
        self.cursor = self.conn.cursor()
        self._criar_tabela()  # Cria a tabela se ela não existir
        self.ganhos = []
        self.despesas = []

    def _criar_tabela(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacao (
        id INTEGER PRIMARY KEY,
        tipo TEXT NOT NULL,
        valor REAL,
        categoria TEXT NOT NULL,
        descricao TEXT NOT NULL,
        data TEXT NOT NULL
        )
''')
        self.conn.commit()



    def adicionar_receita(self, descricao, valor, categoria):
        data = datetime.now().strftime('%d-%m-%Y')  # Pega a data atual
        self.cursor.execute(
        "INSERT INTO transacao (tipo, valor, categoria, descricao, data ) VALUES (?, ?, ?, ?, ?)",
        ('r', valor, categoria, descricao, data )
        )
        self.ganhos.append(valor)
        self.conn.commit()


    def adicionar_despesa(self, descricao, valor, categoria):
        data = datetime.now().strftime('%d-%m-%Y')
        self.cursor.execute(
            "INSERT INTO transacao (tipo, valor, categoria, descricao, data) VALUES (?, ?, ?, ?, ?)",
            ('d',  valor, categoria, descricao, data)  # 'd' de despesa
        )
        self.despesas.append(valor)
        self.conn.commit()


    def Saldo(self, saldo=0):
        if not self.ganhos and not self.despesas:
            return saldo
        saldo += sum(self.ganhos)
        saldo -= sum(self.despesas)
        return saldo

        

    def listar_todas(self):
        self.cursor.execute("SELECT * FROM transacao")
        resultados = self.cursor.fetchall()

        transacoes = []
        for row in resultados:
            transacoes.append({
            "id": row[0],
            "tipo": row[1],
            "valor": row[2],
            "categoria": row[3],
            "descricao": row[4],
            "data": row[5] 
            })
        return transacoes


    def fechar(self):
        self.conn.close()  # Fecha a conexão com o banco
        
