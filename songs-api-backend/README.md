# 🎵 Songs API - Backend Microservice

A standalone FastAPI backend service for retrieving songs.

## 📋 Overview

This is an **independent backend microservice** that:
- ✅ Runs on **port 8000**
- ✅ Provides REST API endpoints
- ✅ Does NOT depend on frontend
- ✅ Can be deployed separately
- ✅ Can be scaled independently

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd songs-api-backend
pip install -r requirements.txt
```

### 2. Run the Service
```bash
python run.py
```

Or use uvicorn directly:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Test the API
```
http://localhost:8000/docs
```

---

## 📁 Directory Structure

```
songs-api-backend/
├── app/                    # Application code
│   ├── __init__.py
│   ├── main.py            # FastAPI setup
│   ├── models.py          # Pydantic models
│   └── routes.py          # API endpoints
├── data/
│   └── songs.json         # Song database
├── tests/
│   └── test_api.py        # Test suite
├── run.py                 # Startup script
├── pyproject.toml         # Project config
├── requirements.txt       # Dependencies
└── .gitignore
```

---

## 🔌 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| GET | `/songs` | Get all songs |
| GET | `/songs/{id}` | Get song by ID |
| GET | `/songs/search/?query=X` | Search by title/artist |
| GET | `/songs/genre/{genre}` | Filter by genre |

---

## 📊 Configuration

The backend runs with default settings:
- **Host**: 0.0.0.0 (accessible from anywhere)
- **Port**: 8000
- **Reload**: Enabled (hot reload on code changes)

To change the port, use:
```bash
uvicorn app.main:app --port 8001
```

---

## 🧪 Run Tests

```bash
python -m pytest tests/test_api.py -v
```

Expected output: **14/14 PASSED** ✅

---

## 🔗 Integration with Frontend

The **frontend service** needs this backend running on:
```
http://localhost:8000
```

Frontend can be on any port (typically 3000, 8080, or just file://)

---

## 📚 Learn More

- [API Documentation](http://localhost:8000/docs)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)

---

## 🆘 Troubleshooting

**Port already in use?**
```bash
uvicorn app.main:app --port 8001
```

**Dependencies missing?**
```bash
pip install -r requirements.txt
```

---

**Backend service ready for production! 🚀**
