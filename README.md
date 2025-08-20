# Kanban Project

A lightweight **Kanban board** built with **Django (backend)**, **Vue.js (frontend)**, and **PostgreSQL**.  
It supports **Boards, Columns, Tasks, Subtasks, and Epics**, allowing teams to manage their workflows in a structured way.

---

## Features

- 🗂️ **Boards & Columns** – organize work visually
- ✅ **Tasks & Subtasks** – track granular progress
- 🧩 **Epics** – group multiple tasks under one big goal
- 🎨 **Task Coloring** – customize cards with colors
- ↔️ **Drag & Drop** – move tasks across columns
- ✏️ **Edit & Delete** – update or remove tasks/columns directly
- 🌐 **REST API** – built with Django REST Framework
- 🚀 **Dockerized Deployment** – Nginx + Gunicorn + PostgreSQL
- 🔒 **CORS + CSRF protection**

---

## Project Structure

```
Kanban/
├── board/          # Django app (models, views, serializers, urls)
├── Kanban/         # Django project settings and wsgi
├── frontend/       # Vue.js frontend app
├── docker/         # Docker-related files (nginx, gunicorn, db)
├── manage.py       # Django entry point
└── README.md       # Documentation
```

---

## Requirements

- Python 3.8+
- Node.js 16+ (for Vue.js frontend)
- Docker & Docker Compose

---

## Installation (Development)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/kanban.git
   cd kanban
   ```

2. Create virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

5. Run Vue.js frontend (inside `frontend/`):
   ```bash
   npm install
   npm run serve
   ```

---

## Running with Docker

1. Build and start containers:
   ```bash
   docker-compose up --build
   ```

2. The services will be available at:
   - **Backend API** → http://localhost:8000/api/
   - **Frontend** → http://localhost:8080/
   - **Nginx (reverse proxy)** → http://localhost/

3. To stop containers:
   ```bash
   docker-compose down
   ```

---

## API Endpoints

- `GET /api/boards/` – list boards
- `POST /api/boards/` – create board
- `GET /api/columns/` – list columns
- `POST /api/columns/` – create column
- `GET /api/tasks/` – list tasks
- `POST /api/tasks/` – create task
- `PATCH /api/tasks/{id}/` – update task (color, title, etc.)
- `DELETE /api/tasks/{id}/` – delete task

---

## Environment Variables

Configure in `.env` file (for Docker):

```
POSTGRES_DB=kanban
POSTGRES_USER=kanban
POSTGRES_PASSWORD=kanban
DEBUG=1
SECRET_KEY=replace_me_in_production
ALLOWED_HOSTS=*
```

---

## Deployment Notes

- Use **Gunicorn** + **Nginx** for production
- Set `DEBUG=0` and a secure `SECRET_KEY`
- Configure persistent volume for PostgreSQL
- Enable HTTPS in Nginx

---

## License

MIT License. Free to use and modify.
