# 📝 Todo App RESTful API

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/FastAPI-0.115+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![ORM](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg)](https://www.sqlalchemy.org/)
[![Database](https://img.shields.io/badge/PostgreSQL-Neon-336791.svg?logo=postgresql&logoColor=white)](https://neon.tech)
[![Deployment](https://img.shields.io/badge/Render-Live-success.svg?logo=render&logoColor=white)](https://todoapp-ba7j.onrender.com)

A robust, secure, and modern **FastAPI** RESTful backend for task and todo management with user authentication. Built with **PostgreSQL**, **SQLAlchemy 2.0 ORM**, **Alembic migrations**, and **JWT-based authorization**, ensuring complete user data isolation and high performance.

---

## 🌐 Live Deployment & Interactive Docs

The API is deployed and accessible online:

- **🚀 Live Base API**: [https://todoapp-ba7j.onrender.com](https://todoapp-ba7j.onrender.com)
- **📑 Interactive Swagger UI**: [https://todoapp-ba7j.onrender.com/docs](https://todoapp-ba7j.onrender.com/docs)
- **📖 ReDoc Documentation**: [https://todoapp-ba7j.onrender.com/redoc](https://todoapp-ba7j.onrender.com/redoc)

---

## 🚀 Key Features

- **🔐 Secure Authentication & Authorization**:
  - Industry-standard password hashing using `bcrypt`.
  - Stateless JSON Web Token (`PyJWT`) authentication.
  - `/signup` endpoint: Register a new account and immediately receive an access token.
  - `/login` endpoint: Authenticate using OAuth2 password flow.

- **📋 Protected Todo Management (CRUD)**:
  - **Strict User Isolation**: Users can only access, create, modify, and delete their own todos.
  - `GET /todos/`: Fetch all todos belonging to the authenticated user.
  - `POST /todos/todocreate`: Create a new todo item.
  - `PUT /todos/{todo_id}`: Update title, description, or completion status (`is_done`).
  - `DELETE /todos/{todo_id}`: Delete a specific todo.

- **🗄️ Database & Schema Management**:
  - Relational PostgreSQL support (Neon serverless or local instance).
  - Clean declarative models powered by **SQLAlchemy 2.0**.
  - Structured, automated schema versioning with **Alembic**.

- **📑 Interactive API Documentation**:
  - Automatically generated OpenAPI specifications with interactive Swagger UI and alternative ReDoc interface.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **[FastAPI](https://fastapi.tiangolo.com/)** | High-performance Python web framework |
| **[Uvicorn](https://www.uvicorn.org/)** | Lightning-fast ASGI server |
| **[SQLAlchemy 2.0](https://www.sqlalchemy.org/)** | SQL toolkit and Object Relational Mapper |
| **[PostgreSQL](https://www.postgresql.org/)** | Production-grade relational database |
| **[psycopg2-binary](https://www.psycopg.org/)** | PostgreSQL database driver |
| **[Alembic](https://alembic.sqlalchemy.org/)** | Database schema migrations |
| **[Pydantic v2](https://docs.pydantic.dev/)** | Data validation and serialization |
| **[PyJWT](https://pyjwt.readthedocs.io/) & [bcrypt](https://github.com/pyca/bcrypt/)** | Secure token handling and cryptographic password hashing |
| **[Poetry](https://python-poetry.org/)** | Modern dependency management and packaging |

---

## 📂 Project Structure

```text
todo_app/
├── alembic/                  # Database migration scripts and versions
│   ├── versions/             # Migration version history
│   └── env.py                # Alembic migration environment
├── src/
│   └── todo_app/
│       ├── __init__.py
│       ├── database.py       # Engine and sessionmaker setup
│       ├── dependencies.py   # Auth dependencies & DB session generator
│       ├── main.py           # FastAPI application entrypoint & middleware
│       ├── models.py         # SQLAlchemy ORM models (User, Todo)
│       ├── security.py       # Password hashing & JWT generation helpers
│       ├── routers/          # Route controllers
│       │   ├── auth.py       # /signup and /login endpoints
│       │   └── todos.py      # Protected /todos CRUD endpoints
│       └── schemas/          # Pydantic schemas for request & response validation
│           ├── todosschema.py
│           └── userschema.py
├── .env.example              # Template for required environment variables
├── alembic.ini               # Alembic configuration
├── pyproject.toml            # Project dependencies and metadata
└── README.md                 # Project documentation
```

---

## ⚙️ Getting Started

### 1. Prerequisites

- **Python 3.11+** installed
- **Poetry** installed ([Install Guide](https://python-poetry.org/docs/#installation)) or standard `pip`
- A **PostgreSQL database** (e.g. [Neon](https://neon.tech) or a local PostgreSQL server)

### 2. Clone the Repository

```bash
git clone https://github.com/hussnainsaeed515/todoapp.git
cd todo_app
```

### 3. Install Dependencies

Install all project dependencies using Poetry:

```bash
poetry install
```

### 4. Environment Configuration

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Open `.env` and fill in your database credentials and secret key:

```env
# Database configuration
DATABASE_URL=postgresql://username:password@host/database?sslmode=require

# Security & JWT Authentication
SECRET_KEY=your-super-secret-key-change-this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🔄 Database Migrations

Apply the latest database migrations using Alembic:

```bash
poetry run alembic upgrade head
```

To create a new migration after updating models:

```bash
poetry run alembic revision --autogenerate -m "describe_migration"
```

---

## ▶️ Running the Application Locally

Start the local development server:

```bash
poetry run uvicorn todo_app.main:app --reload
```

Once running, the application will be accessible at:
- **API Base URL**: `http://127.0.0.1:8000`
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

---

## 📡 API Reference

### 🔐 Authentication

| Method | Endpoint | Description | Auth Required |
|:---:|---|---|:---:|
| `POST` | `/signup` | Register a new user and receive a JWT access token | ❌ |
| `POST` | `/login` | Authenticate with email/password via OAuth2 password form | ❌ |

### 📋 Todos (User-Protected)

| Method | Endpoint | Description | Auth Required |
|:---:|---|---|:---:|
| `GET` | `/todos/` | Retrieve all todos belonging to the logged-in user | ✅ Bearer Token |
| `POST` | `/todos/todocreate` | Create a new todo item | ✅ Bearer Token |
| `PUT` | `/todos/{todo_id}` | Update an existing todo (title, description, is_done) | ✅ Bearer Token |
| `DELETE` | `/todos/{todo_id}` | Delete a specific todo item | ✅ Bearer Token |

---

## 🧪 Testing with Swagger UI

1. Open the interactive docs at **[https://todoapp-ba7j.onrender.com/docs](https://todoapp-ba7j.onrender.com/docs)** (or `http://127.0.0.1:8000/docs` locally).
2. Execute the **`/signup`** or **`/login`** endpoint to receive an `access_token`.
3. Click the **Authorize 🔓** button in the top right corner and paste your token.
4. Now test any of the protected `/todos` endpoints!

---

## 📄 License

This project is licensed under the MIT License - feel free to use and modify it for your projects.
