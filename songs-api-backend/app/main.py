"""
Main FastAPI Application

This is the entry point for the Songs API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import router

# Create the FastAPI application
app = FastAPI(
    title="Songs API",
    description="A simple API to retrieve songs",
    version="1.0.0"
)

# Enable CORS (allows frontend to call this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the songs router
app.include_router(router)


# Root endpoint
@app.get("/", tags=["Root"])
def root():
    """Welcome message and API info"""
    return {
        "message": "Welcome to the Songs API!",
        "endpoints": {
            "all_songs": "GET /songs",
            "song_by_id": "GET /songs/{song_id}",
            "search_songs": "GET /songs/search/?query=search_term",
            "filter_by_genre": "GET /songs/genre/{genre}",
            "docs": "http://localhost:8000/docs",
        }
    }


# Health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    """Check if the API is running"""
    return {"status": "API is running successfully!"}
