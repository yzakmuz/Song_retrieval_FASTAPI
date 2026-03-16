"""
Routes/Endpoints for the Songs API

This module contains all API endpoints for retrieving songs.
"""

from fastapi import APIRouter, HTTPException
from typing import List
import json
from pathlib import Path

from .models import Song

# Create a router to organize endpoints
router = APIRouter(prefix="/songs", tags=["Songs"])


def load_songs() -> List[dict]:
    """Load songs from the songs.json file in the data folder"""
    songs_file = Path(__file__).parent.parent / "data" / "songs.json"
    
    if songs_file.exists():
        with open(songs_file, "r") as f:
            return json.load(f)
    return []


# ============================================================================
# ENDPOINTS
# ============================================================================

@router.get("", response_model=List[Song])
def get_all_songs():
    """
    Retrieve all songs from the database
    
    Returns:
        List of all songs with their details
    """
    songs = load_songs()
    return songs


@router.get("/{song_id}", response_model=Song)
def get_song_by_id(song_id: int):
    """
    Retrieve a specific song by its ID
    
    Args:
        song_id: The unique identifier of the song
        
    Returns:
        The song details if found
        
    Raises:
        HTTPException: If song is not found (404 error)
    """
    songs = load_songs()
    
    for song in songs:
        if song["id"] == song_id:
            return song
    
    raise HTTPException(status_code=404, detail=f"Song with ID {song_id} not found")


@router.get("/search/", tags=["Songs"])
def search_songs(query: str):
    """
    Search for songs by title or artist
    
    Args:
        query: Search term (searches in title and artist)
        
    Returns:
        List of songs matching the search query
    """
    songs = load_songs()
    query_lower = query.lower()
    
    results = [
        song for song in songs
        if query_lower in song["title"].lower() or 
           query_lower in song["artist"].lower()
    ]
    
    return results


@router.get("/genre/{genre}")
def get_songs_by_genre(genre: str):
    """
    Retrieve all songs from a specific genre
    
    Args:
        genre: The genre to filter by
        
    Returns:
        List of songs in the specified genre
    """
    songs = load_songs()
    
    results = [
        song for song in songs
        if song["genre"].lower() == genre.lower()
    ]
    
    if not results:
        raise HTTPException(
            status_code=404, 
            detail=f"No songs found in genre '{genre}'"
        )
    
    return results
