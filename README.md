# 🎵 Songs API - Microservices Architecture

This project is organized as **two independent microservices**:

```
EASS_active_learning/
├── songs-api-backend/          # Backend Microservice (Port 8000)
│   ├── app/                   # FastAPI application
│   ├── data/                  # Database files
│   ├── tests/                 # Test suite
│   ├── run.py                 # Start backend
│   ├── README.md              # Backend docs
│   └── requirements.txt       # Python dependencies
│
├── songs-api-frontend/         # Frontend Microservice (Static Files)
│   ├── index.html             # Main page
│   ├── css/                   # Stylesheets
│   ├── js/                    # JavaScript logic
│   ├── README.md              # Frontend docs
│   └── ...
│
└── songs-api/                  # (Original combined project - can delete)
```

---

## 🎯 Architecture

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Frontend (Microservice #1)                            │
│  - index.html, css/, js/                              │
│  - Port: 8080 (or file://)                            │
│  - Technology: HTML5, CSS3, JavaScript                │
│                                                         │
│                http://localhost:8000                   │
│                ↓         (REST API)       ↑            │
│                                                         │
│  Backend (Microservice #2)                             │
│  - FastAPI, Python                                     │
│  - Port: 8000                                          │
│  - Database: songs.json                                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Running Both Microservices

### **Terminal 1: Start Backend**
```bash
cd songs-api-backend
python run.py
```

Output:
```
🎵 Starting Songs API...
📍 Open http://localhost:8000/docs for interactive documentation
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### **Terminal 2: Start Frontend**
```bash
cd songs-api-frontend
python -m http.server 8080
```

Output:
```
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/)
```

### **Open in Browser**
- **Backend API**: http://localhost:8000/docs
- **Frontend UI**: http://localhost:8080

---

## 📋 Independence & Deployment

### **Backend Characteristics**
- ✅ Independent REST API
- ✅ Can run without frontend
- ✅ Testable independently
- ✅ Can be deployed to cloud (AWS, Azure, Heroku)
- ✅ Can be scaled separately
- ✅ Works with multiple frontends

### **Frontend Characteristics**
- ✅ No server-side code needed
- ✅ Can run from file:// (just open HTML)
- ✅ Can run on different server/port
- ✅ Easy to host on GitHub Pages
- ✅ Can work with different backends
- ✅ Can be deployed separately

---

## 🔄 Communication Flow

```
User
  ↓
Frontend (Browser)
  ↓
"Get all songs" button click
  ↓
JavaScript: fetch('http://localhost:8000/songs')
  ↓
Backend API
  ↓
JSON Response
  ↓
Frontend displays songs
  ↓
User sees data
```

---

## 🐳 Docker Deployment (Optional)

### **Backend Dockerfile**
```dockerfile
FROM python:3.13
WORKDIR /app
COPY songs-api-backend .
RUN pip install -r requirements.txt
CMD ["python", "run.py"]
```

### **Frontend Dockerfile**
```dockerfile
FROM nginx:alpine
WORKDIR /usr/share/nginx/html
COPY songs-api-frontend .
EXPOSE 80
```

### **Docker Compose**
```yaml
version: '3.8'
services:
  backend:
    build: ./songs-api-backend
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
  
  frontend:
    build: ./songs-api-frontend
    ports:
      - "8080:80"
    depends_on:
      - backend
```

---

## 🚀 Deployment Scenarios

### **Scenario 1: Local Development**
- Backend: `python run.py` on port 8000
- Frontend: Open `index.html` directly
- Both on localhost

### **Scenario 2: Separate Servers**
- Backend: Deploy to AWS EC2 (e.g., 54.123.45.67:8000)
- Frontend: Deploy to GitHub Pages
- Update `js/api.js` with backend URL

### **Scenario 3: Docker Compose**
- Both services in Docker containers
- Orchestrated with Docker Compose
- Scales easily

### **Scenario 4: Kubernetes**
- Backend pod + Frontend pod
- Load balancing
- Auto-scaling
- Full microservices pattern

---

## 🔌 API Contract

Both services communicate via REST API:

```
GET /songs
GET /songs/{id}
GET /songs/search/?query=X
GET /songs/genre/{genre}
GET /health
```

---

## ✅ Microservices Checklist

- ✅ Backend independent of frontend
- ✅ Frontend independent of backend
- ✅ Clear API contract
- ✅ Different ports
- ✅ Separate configuration
- ✅ Separate deployment
- ✅ Separate dependencies
- ✅ Can scale independently
- ✅ Can update independently
- ✅ Can fail independently

---

## 📚 Next Steps

1. **Develop**: Edit each service independently
2. **Test**: Test backend with `/docs`, frontend with UI
3. **Deploy**: Push each service separately
4. **Scale**: Add more backend instances if needed
5. **Monitor**: Monitor each service separately

---

**You have a professional microservices architecture! 🚀**
