# Usa uma imagem base oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências do projeto
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expõe a porta 8501 (padrão do Streamlit)
EXPOSE 8501

# Comando para rodar a aplicação
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.enableCORS=false"]
