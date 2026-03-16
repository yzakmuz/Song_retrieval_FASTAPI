# 🎵 Songs API - Frontend Microservice

A standalone web frontend for the Songs API.

## 📋 Overview

This is an **independent frontend microservice** that:
- ✅ Runs as static HTML/CSS/JavaScript
- ✅ Works on any port (no server needed)
- ✅ Does NOT depend on backend to run locally
- ✅ Communicates with backend via REST API
- ✅ Can be deployed separately

---

## 🚀 Quick Start

### 1. Open the Frontend

Just open `index.html` in your browser:

**Option A: Double-click**
- Navigate to `songs-api-frontend/`
- Double-click `index.html`

**Option B: Drag & Drop**
- Drag `index.html` into your browser window

**Option C: Live Server (if using VS Code)**
```
Right-click index.html → Open with Live Server
```

---

## ⚙️ Configuration

The frontend connects to the backend at:
```javascript
const API_BASE_URL = "http://localhost:8000";
```

To change the backend URL, edit `js/api.js`:
```javascript
const API_BASE_URL = "http://your-backend-url:8000";
```

---

## 📁 Directory Structure

```
songs-api-frontend/
├── index.html             # Main HTML
├── css/
│   └── styles.css        # All styling
└── js/
    ├── api.js            # API communication
    └── ui.js             # UI logic & events
```

---

## 🎯 Features

- ✅ View all songs
- ✅ Get song by ID
- ✅ Search by title/artist
- ✅ Filter by genre
- ✅ Statistics dashboard
- ✅ Health check
- ✅ Beautiful responsive UI

---

## 🔗 Integration with Backend

The frontend **expects** a backend running at:
```
http://localhost:8000
```

If the backend is somewhere else, edit `js/api.js`:
```javascript
const API_BASE_URL = "http://192.168.1.100:8000";  // Example: Different IP
```

---

## 📱 Responsive Design

Works great on:
- ✅ Desktop (1200px+)
- ✅ Tablet (768px - 1199px)
- ✅ Mobile (< 768px)

---

## 🚀 Deployment Options

### **Option 1: Static File Server**
```bash
# Using Python
python -m http.server 8080

# Then open: http://localhost:8080
```

### **Option 2: Node.js HTTP Server**
```bash
npx http-server . -p 8080
```

### **Option 3: Docker**
```dockerfile
FROM nginx:alpine
COPY . /usr/share/nginx/html
EXPOSE 80
```

### **Option 4: GitHub Pages**
- Push to GitHub
- Enable GitHub Pages
- Frontend runs free!

---

## 🔧 Customization

### Change Backend URL
Edit `js/api.js` line 1:
```javascript
const API_BASE_URL = "http://your-backend-url";
```

### Change Colors
Edit `css/styles.css`:
```css
.container {
    background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
}
```

### Add More Genres
Edit `index.html` around line 120:
```html
<option value="NewGenre">New Genre</option>
```

---

## 📚 Learn More

- [Learn JavaScript](https://javascript.info/)
- [Learn CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [REST APIs](https://restfulapi.net/)

---

**Frontend service ready for deployment! 🎨**
