/* =============================================================================
   UI.JS - UI Management and Event Handlers
   ============================================================================= */

/**
 * UI Controller - Manages all UI interactions and updates
 */
class UIController {
    /**
     * Display a list of songs
     */
    static displaySongs(songs, containerId) {
        const container = document.getElementById(containerId);

        if (!songs || songs.length === 0) {
            container.innerHTML = '<div class="empty">No songs found</div>';
            return;
        }

        container.innerHTML = songs
            .map(
                (song) => `
            <div class="song-card">
                <div class="song-title">
                    <span class="song-title-icon">🎵</span>
                    ${song.title}
                </div>
                <div class="song-info">
                    <div class="info-item">
                        <span class="info-label">Artist</span>
                        <span class="info-value">${song.artist}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Album</span>
                        <span class="info-value">${song.album}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Year</span>
                        <span class="info-value">${song.year}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Genre</span>
                        <span class="info-value">${song.genre}</span>
                    </div>
                </div>
            </div>
        `
            )
            .join("");
    }

    /**
     * Display an error message
     */
    static displayError(message, containerId) {
        const container = document.getElementById(containerId);
        container.innerHTML = `<div class="error">❌ ${message}</div>`;
    }

    /**
     * Display a success message
     */
    static displaySuccess(message, containerId) {
        const container = document.getElementById(containerId);
        container.innerHTML = `<div class="success">✅ ${message}</div>`;
    }

    /**
     * Display loading message
     */
    static displayLoading(containerId) {
        const container = document.getElementById(containerId);
        container.innerHTML = '<div class="loading">Loading</div>';
    }

    /**
     * Load and display statistics
     */
    static async loadStats() {
        try {
            const songs = await APIService.getAllSongs();
            const genres = [...new Set(songs.map((s) => s.genre))];
            const years = songs.map((s) => s.year);

            document.getElementById("statsContainer").innerHTML = `
                <div class="stat-card">
                    <div class="stat-number">${songs.length}</div>
                    <div class="stat-label">Total Songs</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">${genres.length}</div>
                    <div class="stat-label">Genres</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">${Math.min(...years)}</div>
                    <div class="stat-label">Oldest Year</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">${Math.max(...years)}</div>
                    <div class="stat-label">Newest Year</div>
                </div>
            `;
        } catch (error) {
            console.error("Failed to load statistics:", error);
        }
    }
}

/* =============================================================================
   EVENT HANDLERS
   ============================================================================= */

/**
 * Check API health
 */
async function checkHealth() {
    try {
        const status = await APIService.checkHealth();
        if (status) {
            UIController.displaySuccess(status.status, "healthStatus");
        } else {
            UIController.displayError(
                "API is not responding correctly",
                "healthStatus"
            );
        }
    } catch (error) {
        UIController.displayError(
            "Cannot connect to API. Make sure it's running on http://localhost:8000",
            "healthStatus"
        );
    }
}

/**
 * Get all songs
 */
async function getAllSongs() {
    UIController.displayLoading("allSongsResults");
    try {
        const songs = await APIService.getAllSongs();
        UIController.displaySongs(songs, "allSongsResults");
    } catch (error) {
        UIController.displayError(error.message, "allSongsResults");
    }
}

/**
 * Get song by ID
 */
async function getSongById() {
    const id = document.getElementById("songId").value;
    const container = "byIdResults";

    if (!id) {
        UIController.displayError("Please enter a song ID", container);
        return;
    }

    UIController.displayLoading(container);
    try {
        const song = await APIService.getSongById(id);
        UIController.displaySongs([song], container);
    } catch (error) {
        UIController.displayError(error.message, container);
    }
}

/**
 * Search songs
 */
async function searchSongs() {
    const query = document.getElementById("searchQuery").value;
    const container = "searchResults";

    if (!query) {
        UIController.displayError("Please enter a search term", container);
        return;
    }

    UIController.displayLoading(container);
    try {
        const songs = await APIService.searchSongs(query);
        if (songs.length === 0) {
            UIController.displaySuccess(
                `No songs found matching "${query}"`,
                container
            );
        } else {
            UIController.displaySongs(songs, container);
        }
    } catch (error) {
        UIController.displayError(error.message, container);
    }
}

/**
 * Get songs by genre
 */
async function getByGenre() {
    const genre = document.getElementById("genreSelect").value;
    const container = "genreResults";

    if (!genre) {
        UIController.displayError("Please select a genre", container);
        return;
    }

    UIController.displayLoading(container);
    try {
        const songs = await APIService.getSongsByGenre(genre);
        UIController.displaySongs(songs, container);
    } catch (error) {
        UIController.displayError(error.message, container);
    }
}

/* =============================================================================
   INITIALIZATION
   ============================================================================= */

/**
 * Initialize the application when DOM is loaded
 */
document.addEventListener("DOMContentLoaded", () => {
    UIController.loadStats();
});
