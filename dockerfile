# Usar imagem oficial do Python
FROM python:3.12

# Definir diretório de trabalho
WORKDIR /app

# Copiar os arquivos
COPY ./main.py ./main.py
COPY ./requirements.txt ./requirements.txt
COPY ./ ./

# Instalar dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expor a porta da aplicação
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
