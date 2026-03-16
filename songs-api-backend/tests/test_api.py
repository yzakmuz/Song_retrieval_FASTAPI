"""
Tests for the Songs API

Comprehensive tests for all endpoints and functionality.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Fixture to provide a test client for the API"""
    return TestClient(app)


class TestRootEndpoint:
    """Test the root endpoint"""
    
    def test_root_returns_welcome_message(self, client):
        """Test that root endpoint returns welcome message"""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json()["message"] == "Welcome to the Songs API!"
        assert "endpoints" in response.json()


class TestHealthEndpoint:
    """Test the health check endpoint"""
    
    def test_health_check_returns_ok(self, client):
        """Test that health endpoint returns ok status"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "API is running successfully!"


class TestSongsEndpoints:
    """Test all songs-related endpoints"""
    
    def test_get_all_songs(self, client):
        """Test retrieving all songs"""
        response = client.get("/songs")
        assert response.status_code == 200
        songs = response.json()
        assert isinstance(songs, list)
        assert len(songs) > 0
        # Check song structure
        first_song = songs[0]
        assert "id" in first_song
        assert "title" in first_song
        assert "artist" in first_song
        assert "album" in first_song
        assert "year" in first_song
        assert "genre" in first_song
    
    def test_get_song_by_id_valid(self, client):
        """Test retrieving a song by valid ID"""
        response = client.get("/songs/1")
        assert response.status_code == 200
        song = response.json()
        assert song["id"] == 1
        assert song["title"] == "Bohemian Rhapsody"
        assert song["artist"] == "Queen"
    
    def test_get_song_by_id_invalid(self, client):
        """Test retrieving a song by invalid ID"""
        response = client.get("/songs/99999")
        assert response.status_code == 404
        assert "not found" in response.json()["detail"].lower()
    
    def test_search_songs_by_artist(self, client):
        """Test searching songs by artist"""
        response = client.get("/songs/search/?query=Queen")
        assert response.status_code == 200
        results = response.json()
        assert isinstance(results, list)
        assert len(results) > 0
        # All results should contain "Queen"
        for song in results:
            assert "Queen" in song["artist"] or "Queen" in song["title"]
    
    def test_search_songs_by_title(self, client):
        """Test searching songs by title"""
        response = client.get("/songs/search/?query=Imagine")
        assert response.status_code == 200
        results = response.json()
        assert len(results) > 0
        assert any("Imagine" in song["title"] for song in results)
    
    def test_search_songs_no_results(self, client):
        """Test searching with no matching results"""
        response = client.get("/songs/search/?query=NonexistentBand")
        assert response.status_code == 200
        results = response.json()
        assert len(results) == 0
    
    def test_filter_by_genre_rock(self, client):
        """Test filtering songs by Rock genre"""
        response = client.get("/songs/genre/Rock")
        assert response.status_code == 200
        songs = response.json()
        assert len(songs) > 0
        # All results should be Rock genre
        for song in songs:
            assert song["genre"].lower() == "rock"
    
    def test_filter_by_genre_pop(self, client):
        """Test filtering songs by Pop genre"""
        response = client.get("/songs/genre/Pop")
        assert response.status_code == 200
        songs = response.json()
        assert len(songs) > 0
        for song in songs:
            assert song["genre"].lower() == "pop"
    
    def test_filter_by_invalid_genre(self, client):
        """Test filtering by non-existent genre"""
        response = client.get("/songs/genre/InvalidGenre")
        assert response.status_code == 404
        assert "found" in response.json()["detail"].lower()
    
    def test_filter_by_genre_case_insensitive(self, client):
        """Test that genre filtering is case-insensitive"""
        response1 = client.get("/songs/genre/Rock")
        response2 = client.get("/songs/genre/rock")
        response3 = client.get("/songs/genre/ROCK")
        
        assert response1.status_code == 200
        assert response2.status_code == 200
        assert response3.status_code == 200
        
        # Should return the same number of results
        assert len(response1.json()) == len(response2.json())
        assert len(response2.json()) == len(response3.json())


class TestResponseFormats:
    """Test response data formats and types"""
    
    def test_song_response_types(self, client):
        """Test that song responses have correct types"""
        response = client.get("/songs/1")
        song = response.json()
        
        assert isinstance(song["id"], int)
        assert isinstance(song["title"], str)
        assert isinstance(song["artist"], str)
        assert isinstance(song["album"], str)
        assert isinstance(song["year"], int)
        assert isinstance(song["genre"], str)
    
    def test_list_response_format(self, client):
        """Test that list responses are proper arrays"""
        response = client.get("/songs")
        songs = response.json()
        assert isinstance(songs, list)
        assert all(isinstance(song, dict) for song in songs)
