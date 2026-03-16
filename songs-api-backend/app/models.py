"""
Data models for the Songs API

Pydantic models define the structure and validation for API data.
"""

from pydantic import BaseModel


class Song(BaseModel):
    """
    Song model - represents a single song in the database
    
    Attributes:
        id: Unique identifier for the song
        title: Name of the song
        artist: Artist who performed the song
        album: Album the song is from
        year: Release year
        genre: Music genre
    """
    id: int
    title: str
    artist: str
    album: str
    year: int
    genre: str
