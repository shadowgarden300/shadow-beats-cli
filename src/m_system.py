import sys
queue = []

def play_song(query):
    """search and play the given song"""
    print("play song")

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
    print("play_play_list")

def update_tranding():
    """update system playlists"""
    print("update_tranding")

def list_play_lists():
    """List all the playlists"""
    print("list_play_lists")


def play_current_song():
     """Play current song in queue if not present then figure may be play last payed
     may be keep last plaed song always in queue"""
     print("play_current_song")

def switch_to_video():
     """switch current song to video"""
     print("switch_to_video")

def switch_to_audio():
    """switch current song to audio"""
    print("switch_to_audio")

def play_next_song(): 
     """play next song"""
     print("play next song")

def exit_tool():
     """exit form cli"""
     sys.exit()

def display_queue():
    """list all the songs in queue"""
    print("display_queue")
     
def play_previous_song(): 
     """play previous song"""
     print("play_previous_song")

def repeat_this_song():       
    """repet current song infinitely"""
    print("repeat_this_song")

def save_to_playlist(play_list):
    """save current song to given playlist"""   
    print("save to playlist") 

def pause_current_song():
    """pause currently playing song"""    
