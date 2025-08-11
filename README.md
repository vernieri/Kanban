# 🗂 Kanban Board – Django REST API + Frontend

Sistema de **Kanban Web** desenvolvido em **Django + Django REST Framework** com suporte a **Epics, Tasks e SubTasks**.  
Permite criar quadros, colunas, tasks, subtasks e mover cards por **drag & drop**.

## 🚀 Funcionalidades

- CRUD completo de **Boards**, **Colunas**, **Tasks** e **SubTasks**
- Estrutura hierárquica:
  - **Epic** → várias Tasks
  - **Task** → várias SubTasks
- Reordenação de Tasks via **drag and drop**
- Edição e exclusão **inline**
- Suporte a cores nas Tasks
- Backend em **Django REST Framework**
- Frontend em **HTML + JavaScript**
- Suporte a **CORS**
- **Docker** e **docker-compose** para fácil deploy
- Banco padrão SQLite (dev) e PostgreSQL (prod)

---

## 📂 Estrutura do Projeto

```
Kanban/
├── board/                  # App principal
│   ├── migrations/
│   ├── models.py           # Models: Board, Column, Task, SubTask
│   ├── serializers.py      # Serializers DRF
│   ├── views.py            # Views e API endpoints
│   ├── urls.py             # Rotas do app
│   └── templates/board/    # HTML frontend
│       └── index.html
├── Kanban/                 # Configurações Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── staticfiles/            # Arquivos estáticos coletados
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Instalação (Local)

### 1️⃣ Clonar repositório
```bash
git clone https://github.com/seuusuario/kanban.git
cd kanban
```

### 2️⃣ Criar virtualenv e instalar dependências
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3️⃣ Configurar banco de dados
```bash
python manage.py migrate
```

### 4️⃣ Criar superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 5️⃣ Rodar servidor local
```bash
python manage.py runserver
```
Acesse: **http://127.0.0.1:8000/**

---

## 🐳 Rodando com Docker

### 1️⃣ Build da imagem
```bash
docker-compose build
```

### 2️⃣ Subir containers
```bash
docker-compose up -d
```

### 3️⃣ Criar banco e aplicar migrações
```bash
docker-compose exec web python manage.py migrate
```

### 4️⃣ Criar superusuário (opcional)
```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 🌐 Endpoints da API

### Boards
| Método | Endpoint      | Descrição          |
|--------|--------------|--------------------|
| GET    | `/api/boards/` | Lista todos boards |
| POST   | `/api/boards/` | Cria novo board    |

### Columns
| Método | Endpoint        | Descrição               |
|--------|----------------|-------------------------|
| GET    | `/api/columns/` | Lista colunas           |
| POST   | `/api/columns/` | Cria nova coluna        |
| PATCH  | `/api/columns/{id}/` | Edita coluna        |
| DELETE | `/api/columns/{id}/` | Remove coluna       |

### Tasks
| Método | Endpoint       | Descrição               |
|--------|---------------|-------------------------|
| POST   | `/api/tasks/`  | Cria task               |
| PATCH  | `/api/tasks/{id}/` | Edita task           |
| PATCH  | `/api/tasks/{id}/move/` | Move task       |
| DELETE | `/api/tasks/{id}/` | Remove task          |

### SubTasks
| Método | Endpoint          | Descrição              |
|--------|------------------|------------------------|
| POST   | `/api/subtasks/`  | Cria subtask           |
| PATCH  | `/api/subtasks/{id}/` | Edita subtask       |
| DELETE | `/api/subtasks/{id}/` | Remove subtask      |

---

## 🖥️ Frontend

O **`index.html`** localizado em `board/templates/board/index.html` faz chamadas AJAX para a API usando `fetch()` e renderiza o Kanban com:

- **Drag and Drop** para mover tasks
- Botões para criar, editar e excluir
- Seção expansível de **SubTasks**

---

## 🔐 Variáveis de Ambiente

| Variável                | Padrão        | Descrição                  |
|-------------------------|--------------|----------------------------|
| `DJANGO_DEBUG`          | `1`          | Ativa modo debug           |
| `DJANGO_SECRET_KEY`     | `unsafe-dev` | Chave secreta Django       |
| `DJANGO_ALLOWED_HOSTS`  | `*`          | Hosts permitidos           |
| `DB_ENGINE`             | `sqlite`     | Banco (`sqlite` ou `postgres`) |
| `POSTGRES_DB`           | `kanban`     | Nome do banco (Postgres)   |
| `POSTGRES_USER`         | `kanban`     | Usuário do banco           |
| `POSTGRES_PASSWORD`     | `senha`      | Senha do banco             |
| `POSTGRES_HOST`         | `db`         | Host do Postgres           |
| `POSTGRES_PORT`         | `5432`       | Porta do Postgres          |
| `CORS_ALLOW_ALL`        | `1`          | Libera todos domínios CORS |

---

## 📜 Licença

Este projeto é distribuído sob a licença MIT.  
Sinta-se livre para usar e modificar.
