# import yt_dlp
# import time
# import requests

# def fetch_combined_stream(formats):
#     """Extract the first combined audio+video stream URL from the formats."""
#     return next((f['url'] for f in formats if f.get('vcodec') != 'none' and f.get('acodec') != 'none'), None)

# def get_audio_video_combined_url(video_id):
#     """
#     Given a YouTube video ID, extract the combined stream URL.
#     """
#     url = f"https://www.youtube.com/watch?v={video_id}"
#     ydl_opts = {
#         'quiet': True,
#         'noplaylist': True
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.extract_info(url, download=False)
#         formats = info_dict.get('formats', [])
#         return fetch_combined_stream(formats)

# def get_stream_url_from_query(query):
#     """
#     Use yt-dlp's search to get the first video result and return its combined stream URL.
#     """
#     ydl_opts = {
#         'quiet': True,
#         'noplaylist': True,
#         'default_search': 'ytsearch1'
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(query, download=False)
#         # When search returns a playlist, pick the first entry
#         video = info['entries'][0] if 'entries' in info else info
#         formats = video.get('formats', [])
#         return fetch_combined_stream(formats)

# def get_video_id_via_youtube_search_api(query, api_key):
#     """
#     Use the YouTube Data API to search for a video matching the query.
#     """
#     search_url = "https://www.googleapis.com/youtube/v3/search"
#     params = {
#         'part': 'snippet',
#         'q': query,
#         'key': api_key,
#         'maxResults': 1,
#         'type': 'video'
#     }
#     response = requests.get(search_url, params=params)
#     data = response.json()
#     if 'items' in data and len(data['items']) > 0:
#         return data['items'][0]['id']['videoId']
#     return None

# def get_stream_url_via_api(query, api_key):
#     """
#     Use the YouTube API to get a video ID then fetch the combined stream URL with yt-dlp.
#     """
#     video_id = get_video_id_via_youtube_search_api(query, api_key)
#     if video_id:
#         return get_audio_video_combined_url(video_id)
#     return None

# if __name__ == '__main__':
#     test_query = "khalasi"
#     # Replace with your actual YouTube Data API key
#     api_key = "AIzaSyAfAuIkwtgx1EXDjBvdEQOdQFcA2F8mI5U"

#     # Approach 1: Using yt-dlp search directly
#     start_time = time.time()
#     url_from_query = get_stream_url_from_query(test_query)
#     duration_query = time.time() - start_time

#     print("yt-dlp search approach:")
#     print("Combined Stream URL:", url_from_query)
#     print("Duration: {:.2f} seconds".format(duration_query))

#     # Approach 2: Using YouTube API search then yt-dlp extraction
#     start_time = time.time()
#     url_from_api = get_stream_url_via_api(test_query, api_key)
#     duration_api = time.time() - start_time

#     print("\nYouTube API search approach:")
#     print("Combined Stream URL:", url_from_api)
#     print("Duration: {:.2f} seconds".format(duration_api))

    
def function():
    return {
        'title':"hello world"
    }

obj = function()
obj['id'] = 123
print(obj)