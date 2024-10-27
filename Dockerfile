# Use a imagem oficial do Python com a última versão
FROM python:latest

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copie o código da aplicação para o diretório de trabalho no container
COPY . .

# Exponha a porta padrão do Django
EXPOSE 8000

# Copie o script de entrada e torne-o executável
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Defina o script de entrada como comando padrão
ENTRYPOINT ["/entrypoint.sh"]