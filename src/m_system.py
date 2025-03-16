import sys
import youtube
import mpv

queue = []
psudo_queue = []
player = mpv.MPV()
current_song={}
CACHE_DIR="./"
def play_song(query):
    """search and play the given song"""
    song = youtube.get_song(query)
    song['index'] = 0
    global queue,current_song
    queue = [song]
    current_song=song
    play_queue(0)
    

def play_song_video(query):
    """search and play the given song video""" 
    print("play_song_video")

def list_all_songs(play_list):
    """List all songs in given playlist"""
    print("list_all_songs")

def delete_song(play_list,song):
    """delete given playlist song"""
    print("delete_song")

def play_play_list(play_list):
    """Add all the songs in given play list to queue and play the queue"""
    #if playlist is system playlist then check when it was updated and based on time update
    play_queue(0)
    


def update_tranding():
    """update system playlists"""
    print("update_tranding")

def list_play_lists():
    """List all the playlists"""
    print("list_play_lists")


def play_queue(index):
    """Play current song in queue if not present then figure may be play last payed
    may be keep last plaed song always in queue"""
    for song in queue:
        if current_song['index'] < index:
            continue
        global current_song
        current_song=queue[index]
        player.play(current_song['url'])
        if index == len(queue):
            load_recommended_songs(current_song)
        #cache next song
        cache_song(index+1)

def play_current_song():
    """play the song"""
    player.pause = False    

def switch_to_video():
     """switch current song to video"""
     print("switch_to_video")

def switch_to_audio():
    """switch current song to audio"""
    print("switch_to_audio")

def play_next_song(): 
     """play next song"""
     if len(queue) < current_song['index']+1:
         load_recommended_songs(current_song)
     play_queue(current_song['index']+1) 
    
     
def exit_tool():
     """exit form cli"""
     sys.exit()

def display_queue():
    """list all the songs in queue"""
    for index, song in enumerate(queue):
        if song['index'] == current_song['index']:
            print(index, ".", song['title'], " *")
        else:
            print(index, ".", song['title'])
     
def play_previous_song(): 
     """play previous song"""
     if len(queue) < current_song['index']-1:
         print("no previous song")
         return
     play_queue(current_song['index']-1) 

def repeat_this_song():       
    while True:
        player.play(current_song['url'])

def save_to_playlist(play_list):
    """save current song to given playlist"""   
    print("save to playlist") 

def pause_current_song():
    """pause currently playing song""" 
    player.pause = True 

def add_to_queue(query):
    """add song to queue"""
    print(query)
    song = youtube.get_song(query)
    song['index'] = current_song['index']+1
    queue.insert(current_song['index']+1,song)
    print("Added to queue")

def cache_song (index):
    """get url for the index from queue"""
    video_id = queue[index]['video_id']
    song = youtube.get_audio_video_combined_url_and_video_data(video_id)
    queue.remove(index)
    queue.insert(index,song)  

def load_recommended_songs(song):
    """find recommended songs and add them to queue""" 
    print("loading more songs...")     
    #load from api with video_id
  
