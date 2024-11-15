# Projeto do programa de Pós graduação em Engenharia de Software - PUC Minas

## Project Setup and Management

### Table of Contents
- [Environment Setup](#environment-setup)
- [Database Management](#database-management)
- [Docker Deployment](#docker-deployment)
- [Live Project](#live-project)
- [Demo Videos](#demo-videos)
- [Access Credentials](#access-credentials)

### Environment Setup
1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Database Management
1. Create migrations:
   ```bash
   python manage.py makemigrations
   ```

2. Apply migrations:
   ```bash
   python manage.py migrate
   ```

### Docker Deployment
1. Build and run the Docker container:
   ```bash
   docker rm -f workshops && docker build -t workshops . && docker run -d -p 8000:8000 --name workshops-new workshops
   ```
2. Open in your browser: [http://localhost:8000](http://localhost:8000)


### Live Project
The project is live at [workshops.edersilva.com](https://workshops.edersilva.com/)

### Demo Videos
- [Frontend Demo](https://youtu.be/p7DdTj2yGVc)
- [Backend Demo](https://youtu.be/pLRZwyz2L_E)

Additional video resources can be found in the [videos directory](https://github.com/edersilva/workshop/tree/main/videos).

### Access Credentials

#### Administrator Access
- **URL:** [workshops.edersilva.com/admin](https://workshops.edersilva.com/admin)
- **Username:** puc
- **Password:** admin123

#### User Access
- **URL:** [workshops.edersilva.com](https://workshops.edersilva.com)
- **Username:** heitor@pucminas.com
- **Password:** meufilho