"""
Run the Songs API

Simple script to start the FastAPI server.
"""

import uvicorn
from app.main import app

if __name__ == "__main__":
    print("🎵 Starting Songs API...")
    print("📍 Open http://localhost:8000/docs for interactive documentation")
    print("🌐 Open http://localhost:8000 for API info")
    print("Press CTRL+C to stop the server\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
