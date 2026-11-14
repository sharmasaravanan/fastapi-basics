# FastAPI Power Operations Health Monitor

A simulated Power Operations Health Monitor API built with FastAPI. Demonstrates API key authentication, equipment readings, alert management with status filtering, and Docker containerization.

> ⚠️ **This application uses simulated data only.** Nothing connects to real power equipment.

## 🚀 Features

- **API Key Authentication** — Header-based API key security (`access_token`)
- **Equipment Readings** — List all readings or query by equipment ID
- **Alert Management** — Filter alerts by status (`active` / `resolved`)
- **Environment Configuration** — Configurable via environment variables
- **Docker Support** — Production-ready Dockerfile included

## 📁 Project Structure

```
.
├── fastapi_power_app.py  # Main application
├── Dockerfile            # Container build instructions
├── requirements.txt      # Python dependencies
└── .dockerignore         # Files excluded from Docker build
```

## 🛠️ Tech Stack

- **Python 3.9**
- **FastAPI** — High-performance API framework
- **Pydantic** — Data validation and serialization
- **Uvicorn** — ASGI server

## ⚡ Quick Start

### Run Locally

```bash
pip install -r requirements.txt
uvicorn fastapi_power_app:app --host 0.0.0.0 --port 8000 --reload
```

### Run with Docker

```bash
docker build -t power-ops-monitor .
docker run -p 8000:8000 -e APP_ENV=production power-ops-monitor
```

### Test the API

```bash
# Home — no auth required
curl http://localhost:8000/

# Health check
curl http://localhost:8000/health

# List readings (requires API key)
curl -H "access_token: 1234567asdfgh" http://localhost:8000/readings

# Get specific equipment reading
curl -H "access_token: 1234567asdfgh" http://localhost:8000/readings/SUB-101

# List all alerts
curl http://localhost:8000/alerts

# Filter active alerts only
curl http://localhost:8000/alerts?status=active
```

## 📖 API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/` | No | Application info |
| GET | `/health` | No | Health status |
| GET | `/readings` | ✅ API Key | List all equipment readings |
| GET | `/readings/{equipment_id}` | ✅ API Key | Get reading by equipment ID |
| GET | `/alerts` | No | List alerts (optional `?status=` filter) |

## 🔐 Authentication

Include the API key in the request header:

```
access_token: 1234567asdfgh
```

## 📚 Interactive Docs

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

