# Shadow-Beats-CLI 

Shadow-Beats-CLI is a free music application that allows you to play music via a command-line interface (CLI). It supports searching for songs, managing playlists, and provides a seamless music playback experience with a virtual queue and caching system.

## Features

### Base Flags (CLI Usage)

Run the CLI with `sbeats` followed by these flags:

1.  `-s` or `--search <search_term>`
    * Searches YouTube using the provided string and plays the first result.
    * Example: `shadow-beats-cli -s khalasi`

2.  `-p` or `--playlist <playlist_name>`
    * Plays songs from the specified playlist.
    * Sub-flags:
        * `-a` or `--audio`: Plays audio only (default).
        * `-v` or `--video`: Plays video.
        * `-ls` or `--listsongs`: Lists all songs in the playlist.
        * `-d` or `--delete <song_name>`: Deletes the specified song from the playlist.
    * Example: `shadow-beats-cli -p my_playlist -v`
    * Note: Playlists are of two types:
        * **User Playlists**: Custom playlists created by the user.
        * **System Playlists**: Predefined playlists that update over time.

3.  `-u` or `--update`
    * Updates all system playlists.
    * Example: `shadow-beats-cli -u`

4.  `-l` or `--list`
    * Lists all available playlists (user and system).
    * Example: `shadow-beats-cli -l`

### Non-Base Commands (Interactive Mode)

Once the CLI is running, you can use these commands:

* `pause`: Pauses the current song.
* `play`: Resumes playback.
* `video`: Switches the current song to video mode.
* `audio`: Switches the current song to audio-only mode.
* `next`: Skips to the next song in the queue.
* `exit`: Exits the CLI.
* `save <playlist_name>`: Saves the current song to the specified playlist (defaults to "liked_songs" if no name provided).
* `nextall`: Lists the next songs in the queue.
* `previous`: Plays the previous song.
* `repeat`: Toggles repeat mode for the current song.
* `add <song_name>`: Adds a song to the queue by name.

### Queueing

* The next song in the queue plays automatically after the current song ends.
* A virtual queue caches the next three songs for smooth playback.

### Recommendations

* If the current song is the last in the queue, recommended songs are automatically added based on the current song.

## Setup Instructions

### Prerequisites

* Python 3.8+
* Git
* YouTube Data API Key (from Google Cloud Console)
* A directory for caching songs

### Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/yourusername/shadow-beats-cli.git](https://github.com/yourusername/shadow-beats-cli.git)
    cd shadow-beats-cli
    ```

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Set up environment variables:
    * `YOUTUBE_API_KEY`: Required for accessing the YouTube Data API.
    * `CACHE_DIR_PATH`: Directory path for caching songs.

    Example (Linux/Mac):

    ```bash
    export YOUTUBE_API_KEY="your-youtube-api-key"
    export CACHE_DIR_PATH="/path/to/cache/directory"
    ```

    Example (Windows):

    ```cmd
    set YOUTUBE_API_KEY=your-youtube-api-key
    set CACHE_DIR_PATH=C:\path\to\cache\directory
    ```

4.  Run the CLI:

    ```bash
    python shadow-beats-cli.py
    ```

### Environment Variables

| Variable          | Description                               | Example Value                  |
| :---------------- | :---------------------------------------- | :----------------------------- |
| `YOUTUBE_API_KEY` | YouTube Data API key for song search      | `AIzaSy...`                    |
| `CACHE_DIR_PATH`  | Directory to cache songs for playback     | `/home/user/shadow_beats_cache` |

## Usage Examples

* Search and play a song:

    ```bash
    sbeats -s "khalasi"
    ```

* Play a playlist with video:

    ```bash
    sbeats -p "my_playlist" -v
    ```

* List all playlists:

    ```bash
    sbeats -l
    ```

* Update system playlists:

    ```bash
    sbeats -u
    ```

## Contributing

Feel free to fork this repository, submit issues, or create pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.