# Python slim moderno (pode trocar p/ 3.12 se quiser)
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# deps do sistema (psycopg para Postgres em prod)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

# dependências python (ajuste versões se quiser fixar)
RUN pip install "django>=4.2,<5" djangorestframework django-cors-headers gunicorn whitenoise psycopg2-binary

# copia o projeto
COPY Kanban/ /app/Kanban
WORKDIR /app/Kanban

# porta do runserver/gunicorn
EXPOSE 8000

# por padrão, roda runserver (dev). No compose de prod a gente sobrescreve.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
