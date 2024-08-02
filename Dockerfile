# Usar imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar arquivos de requisitos
COPY requirements.txt requirements.txt

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Definir a variável de ambiente
ENV PYTHONUNBUFFERED=1

# Comando padrão para rodar a aplicação
CMD ["python", "src/main.py"]