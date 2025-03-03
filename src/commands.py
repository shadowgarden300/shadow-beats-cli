import argparser
import m_system

parser = argparser.ArgumentParser(discription="parse base arguments")

parser.add_argument("-s", "--search", help="search and play given song", type=str)
parser.add_argument("-p", "--playlist", help="Play the songs in given playlist", type=str)
parser.add_argument("-u", "--update", help="Update given m_system playlist", type=str)
parser.add_argument("-l", "--list", help="List all the playlists", type=str)
parser.add_argument("-a", "--audio", help="Play the song only audio default behiviour used with -s", type=str)
parser.add_argument("-v", "--video", help="Play the song only video used with -s", type=str)
parser.add_argument("-ls", "--listsongs", help="List given playlist songs used with -p", type=str)
parser.add_argument("-d", "--delete", help="Delete the song in given playlist used with -p", type=str)


args = parser.parse_args()

if args.s:
    if args.a:
        m_system.play_song(args.s) 
    elif args.v:
        m_system.play_song_video(args.s)
    else:    
        m_system.play_song(args.s)
elif args.p: 
    if args.ls: 
        m_system.list_all_songs(args.p)
    elif args.d:
        m_system.delete_song(args.p,args.d)
    else:                  
        m_system.play_play_list(args.p)  
elif args.u:
    m_system.update_tranding()
elif args.l:
    m_system.list_play_lists() 
else:
    print('Unkown command');       


# def validate_runtime_input(cmd):
#     if cmd == 'exit':
        
