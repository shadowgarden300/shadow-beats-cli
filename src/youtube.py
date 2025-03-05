import yt_dlp
import os
import requests

YOUTUBE_API_KEY=os.getenv("YOUTUBE_API_KEY")

def get_song(query):
    video_id = get_video_via_youtube_search_api(query)
    if  video_id == None:
        print("No video found")
        return
    video = get_audio_video_combined_url_and_video_data(video_id)

    if video:
        return video
    print("No video found")

def get_video_via_youtube_search_api(query):
    """
    Use the YouTube Data API to search for a video matching the query.
    Returns the video ID or None if an error occurs.
    """
    try:
        if not YOUTUBE_API_KEY:
            print("Error: YouTube API key is missing.")
            return None
        
        search_url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            'part': 'snippet',
            'q': query,
            'key': YOUTUBE_API_KEY,
            'maxResults': 1,
            'type': 'video'
        }
        
        response = requests.get(search_url, params=params, timeout=5)
        response.raise_for_status()  # Raise HTTP errors
        
        data = response.json()
        
        if 'items' in data and data['items']:
            return data['items'][0]['id']['videoId']
        
        print(f"Warning: No video found for query '{query}'")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def fetch_combined_stream(formats):
    """Extract the first combined audio+video stream URL from the formats."""
    return next((f['url'] for f in formats if f.get('vcodec') != 'none' and f.get('acodec') != 'none'), None)

def get_audio_video_combined_url_and_video_data(video_id):
    """
    Given a YouTube video ID, extract the combined stream URL.
    """

    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        ydl_opts = {
            'quiet': True,
            'noplaylist': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            title = info_dict.get('title', 'Unknown Title')
            tags = info_dict.get('tags', [])
            combined_stream_url = fetch_combined_stream(formats)
            
            return {
                "title": title,
                "tags": tags,
                "url": combined_stream_url
            }
    except:
        return None   
    

    
