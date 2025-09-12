# Usar imagem oficial do Python
FROM python:3.12

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências
# Copiamos primeiro o requirements.txt e instalamos as dependências.
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Agora copiamos o resto do código da aplicação
COPY . .

# Expor a porta da aplicação
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
