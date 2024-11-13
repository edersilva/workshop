# Project Setup and Management

## Environment Setup

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Database Management

3. Create migrations:
   ```bash
   python manage.py makemigrations
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

## Populating the Database

You can populate the database with sample data using the following commands:

Criar os professores
python manage.py populate_professors 10

Criar as aulas
python manage.py populate_lessons 10

Criar os workshops
python manage.py populate_workshops 10

Criar os usuários
python manage.py populate_users 10

Criar os favoritos
python manage.py populate_favorites 10

Criar os comentários
python manage.py populate_reviews 10

Criar os certificados
python manage.py populate_certificates 10

Ou
python manage.py populate_all

Limpar todos os dados
python manage.py flush



docker build -t workshops . && docker run -d -p 8000:8000 --name workshops workshops

http://localhost:8000

docker ps 

docker logs workshops

docker stop workshops

docker rm workshops

docker rmi workshops
