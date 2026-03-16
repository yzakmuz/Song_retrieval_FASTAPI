/* =============================================================================
   API.JS - API Communication Layer
   ============================================================================= */

const API_BASE_URL = "http://localhost:8000";

/**
 * API Service - Handles all communication with the backend
 */
class APIService {
    /**
     * Check API health status
     */
    static async checkHealth() {
        try {
            const response = await fetch(`${API_BASE_URL}/health`);
            return response.ok ? response.json() : null;
        } catch (error) {
            throw new Error(`Health check failed: ${error.message}`);
        }
    }

    /**
     * Get all songs
     */
    static async getAllSongs() {
        try {
            const response = await fetch(`${API_BASE_URL}/songs`);
            if (!response.ok) throw new Error('Failed to fetch songs');
            return await response.json();
        } catch (error) {
            throw new Error(`Failed to get all songs: ${error.message}`);
        }
    }

    /**
     * Get a single song by ID
     */
    static async getSongById(id) {
        try {
            const response = await fetch(`${API_BASE_URL}/songs/${id}`);
            if (response.status === 404) {
                throw new Error(`Song with ID ${id} not found`);
            }
            if (!response.ok) throw new Error('Failed to fetch song');
            return await response.json();
        } catch (error) {
            throw new Error(`Failed to get song: ${error.message}`);
        }
    }

    /**
     * Search songs by query (title or artist)
     */
    static async searchSongs(query) {
        try {
            if (!query.trim()) {
                throw new Error('Search query cannot be empty');
            }
            const url = `${API_BASE_URL}/songs/search/?query=${encodeURIComponent(query)}`;
            const response = await fetch(url);
            if (!response.ok) throw new Error('Search failed');
            return await response.json();
        } catch (error) {
            throw new Error(`Search failed: ${error.message}`);
        }
    }

    /**
     * Get songs by genre
     */
    static async getSongsByGenre(genre) {
        try {
            if (!genre) {
                throw new Error('Genre must be selected');
            }
            const response = await fetch(`${API_BASE_URL}/songs/genre/${genre}`);
            if (response.status === 404) {
                throw new Error(`No songs found in genre '${genre}'`);
            }
            if (!response.ok) throw new Error('Failed to fetch songs');
            return await response.json();
        } catch (error) {
            throw new Error(`Failed to get songs by genre: ${error.message}`);
        }
    }
}
