# django-project-structure

A Django-based web platform with modular apps, REST API (DRF), JWT authentication, Stripe subscriptions, and a production-ready structure.

---

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Auth**: JWT (SimpleJWT), Custom User Model
- **Database**: PostgreSQL
- **Queue**: Redis
- **Container**: Docker & docker-compose
- **Testing**: Pytest + Coverage
- **Structure**: Modular app-based directory layout

---

## Project Structure (Simplified)
```bash
├── apps/ # Core apps: users, payments, example, etc.
│ └── users/
│ └── api/v1/
├── config/ # Django settings, wsgi/asgi, etc.
├── requirements/ # Separate requirements per environment
├── deployments/ # Docker & compose files
├── manage.py
├── README.md
└── .env
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourname/yourproject.git
cd yourproject
```

2. Create & Configure `.env` File

3. Run Server
```bash
docker compose up --build
docker compose exec web bash
uv run bash setup.sh
```
