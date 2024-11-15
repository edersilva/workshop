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

1. Create migrations:
   ```bash
   python manage.py makemigrations
   ```

2. Apply migrations:
   ```bash
   python manage.py migrate
   ```

## Docker Deployment

1. Build and run the Docker container:
   ```bash
   docker build -t workshops . && docker run -d -p 8000:8000 --name workshops workshops
   ```

2. Access the application at:
   ```
   http://localhost:8000
   ```

## Live Project
<a href="https://workshops.edersilva.com/" target="_blank">https://workshops.edersilva.com/</a>

## Test User Credentials

### Administrator Access
- **URL:** <a href="https://workshops.edersilva.com/admin" target="_blank">https://workshops.edersilva.com/admin</a>
- **Username:** puc
- **Password:** admin123

### User Access
- **URL:** <a href="https://workshops.edersilva.com" target="_blank">https://workshops.edersilva.com</a>
- **Username:** heitor@pucminas.com
- **Password:** meufilho