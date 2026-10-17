# 📝 Todo App API

Ek modern aur secure **FastAPI** based RESTful API jo user authentication aur personal todo management provide karti hai. Is project mein **PostgreSQL**, **SQLAlchemy ORM**, **Alembic migrations**, aur **JWT authentication** ka istemal kiya gaya hai.

---

## 🚀 Features

- **🔐 User Authentication & Authorization**:
  - Secure password hashing using `bcrypt`.
  - JWT (JSON Web Tokens) authentication using `PyJWT`.
  - `/signup`: Naya user register karna aur foran access token hasil karna.
  - `/login`: OAuth2 password form ke zariye login aur token generation.

- **📋 Todo CRUD Operations (Protected)**:
  - Har user sirf apne hi todos access, create, update, aur delete kar sakta hai (user isolation).
  - `GET /todos/`: Current logged-in user ke sabhi todos dekhna.
  - `POST /todos/todocreate`: Naya todo create karna.
  - `PUT /todos/{todo_id}`: Todo ka title, description, ya status (`is_done`) update karna.
  - `DELETE /todos/{todo_id}`: Todo delete karna.

- **🗄️ Database & Migrations**:
  - PostgreSQL database support (Neon serverless ya local PostgreSQL).
  - SQLAlchemy 2.0 ORM models (`User`, `Todo`).
  - Alembic ke zariye structured database migrations.

- **📑 Interactive API Documentation**:
  - Auto-generated Swagger UI docs (`/docs`).
  - ReDoc documentation (`/redoc`).

---

## 🛠️ Tech Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
- **Database ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Database Driver**: [psycopg2-binary](https://www.psycopg.org/)
- **Migrations**: [Alembic](https://alembic.sqlalchemy.org/)
- **Validation & Schemas**: [Pydantic v2](https://docs.pydantic.dev/)
- **Security & Tokens**: [PyJWT](https://pyjwt.readthedocs.io/), [bcrypt](https://github.com/pyca/bcrypt/)
- **Dependency Management**: [Poetry](https://python-poetry.org/)

---

## 📂 Project Structure

```text
todo_app/
├── alembic/                  # Database migration scripts
│   ├── versions/             # Migration version history
│   └── env.py                # Alembic environment config
├── src/
│   └── todo_app/
│       ├── __init__.py
│       ├── database.py       # Engine aur database session setup
│       ├── dependencies.py   # Auth dependencies & get_db session generator
│       ├── main.py           # FastAPI application entrypoint
│       ├── models.py         # SQLAlchemy database models (User, Todo)
│       ├── security.py       # Password hashing & JWT creation utilities
│       ├── routers/          # API Route handlers
│       │   ├── auth.py       # /signup aur /login endpoints
│       │   └── todos.py      # /todos CRUD endpoints
│       └── schemas/          # Pydantic models for validation & serialization
│           ├── todosschema.py
│           └── userschema.py
├── .env.example              # Environment variables template
├── alembic.ini               # Alembic configuration
├── pyproject.toml            # Poetry dependencies & project configuration
└── README.md                 # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- **Python 3.11+**
- **Poetry** (Ya standard `pip`)
- **PostgreSQL Database** (e.g., [Neon.tech](https://neon.tech/) ya local PostgreSQL)

### 2. Clone the Repository
```bash
git clone <repository-url>
cd todo_app
```

### 3. Install Dependencies
Poetry ke zariye dependencies install karein:
```bash
poetry install
```

### 4. Configure Environment Variables
`.env.example` file ko copy kar ke `.env` banayein:
```bash
cp .env.example .env
```

`.env` file khol kar apni database details aur secret keys configure karein:
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

Alembic migrations apply karne ke liye yeh command chalayein:

```bash
poetry run alembic upgrade head
```

Agar models mein koi tabdeeli ki ho to nayi migration generate karne ke liye:
```bash
poetry run alembic revision --autogenerate -m "description_of_changes"
```

---

## ▶️ Running the Application

Development server start karne ke liye:

```bash
poetry run uvicorn todo_app.main:app --reload
```

Server chalne ke baad:
- **API URL**: `http://127.0.0.1:8000`
- **Interactive Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc Documentation**: `http://127.0.0.1:8000/redoc`

---

## 📡 API Endpoints

### Authentication (`/`)
| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/signup` | Naya user register karein | ❌ |
| `POST` | `/login` | Email aur password se login karein (OAuth2 Form) | ❌ |

### Todos (`/todos`)
| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/todos/` | Current user ke sabhi todos dekhein | ✅ Bearer Token |
| `POST` | `/todos/todocreate` | Naya todo create karein | ✅ Bearer Token |
| `PUT` | `/todos/{todo_id}` | Todo update karein | ✅ Bearer Token |
| `DELETE` | `/todos/{todo_id}` | Todo delete karein | ✅ Bearer Token |

---

## 🧪 Testing API via Swagger UI

1. Browser mein `http://127.0.0.1:8000/docs` open karein.
2. Pehle `/signup` ya `/login` endpoint se token hasil karein.
3. Top right par **Authorize 🔓** button par click karein aur apna token paste karein.
4. Ab sabhi protected `/todos` endpoints ko test karein!


