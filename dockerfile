# Use a imagem oficial do Python baseada em Debian
FROM python:3.8-slim-buster

# Define o diretório de trabalho no Docker
WORKDIR /app

# Atualiza o sistema e instala as dependências necessárias
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        default-libmysqlclient-dev \
        gcc \
    && rm -rf /var/lib/apt/lists/*

# Instala as dependências do projeto
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto para o Docker
COPY . /app

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8500"]
