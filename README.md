
Ativar o ambiente virtual
source venv/bin/activate

Instalar as dependências
pip install -r requirements.txt


Criar as migrações
python manage.py makemigrations

Migrar
python manage.py migrate

Criar um super usuário
python manage.py createsuperuser

Criar os professores
python manage.py populate_professors 10

Criar as aulas
python manage.py populate_lessons 10

Criar os workshops
python manage.py populate_workshops 20

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