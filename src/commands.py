import argparse
import m_system
import sys

parser = argparse.ArgumentParser(description="parse base arguments")
parser.add_argument("-s", "--search", help="search and play given song", type=str)
parser.add_argument("-p", "--playlist", help="Play the songs in given playlist", type=str)
parser.add_argument("-u", "--update", help="Update given m_system playlist", type=str)
parser.add_argument("-l", "--list", help="List all the playlists", type=str)
parser.add_argument("-a", "--audio", help="Play the song only audio default behavior used with -s", action="store_true")
parser.add_argument("-v", "--video", help="Play the song only video used with -s", action="store_true")
parser.add_argument("-ls", "--listsongs", help="List given playlist songs used with -p", action="store_true")
parser.add_argument("-d", "--delete", help="Delete the song in given playlist used with -p", type=str)

args = parser.parse_args()

if args.search:
    if args.audio:
        m_system.play_song(args.search)
    elif args.video:
        m_system.play_song_video(args.search)
    else:
        m_system.play_song(args.search)
elif args.playlist:
    if args.listsongs:
        m_system.list_all_songs(args.playlist)
    elif args.delete:
        m_system.delete_song(args.playlist, args.delete)
    else:
        m_system.play_play_list(args.playlist)
elif args.update:
    m_system.update_tranding()
elif args.list:
    m_system.list_play_lists()
else:
    print('Unknown command')
    sys.exit()

def validate_runtime_input(command):
    runtime_parser = argparse.ArgumentParser(description="Runtime commands")
    runtime_parser.add_argument('-s', '--search', type=str, help='Search and play song')
    runtime_parser.add_argument('-p', '--playlist', type=str, help='Playlist operations')
    runtime_parser.add_argument('-a', '--audio', action='store_true', help='Audio only')
    runtime_parser.add_argument('-v', '--video', action='store_true', help='Video only')
    runtime_parser.add_argument('-ls', '--listsongs', action='store_true', help='List songs')
    runtime_parser.add_argument('-d', '--delete', type=str, help='Delete song')
    
    try:
        command_parts = command.split()
        args, unknown = runtime_parser.parse_known_args(command_parts)
        
        if args.search:
            if args.audio:
                m_system.play_song(args.search)
            elif args.video:
                m_system.play_song_video(args.search)
            else:
                m_system.play_song(args.search)
        elif args.playlist:
            if args.listsongs:
                m_system.list_all_songs(args.playlist)
            elif args.delete:
                if args.delete:
                    m_system.delete_song(args.playlist, args.delete)
                else:
                    print("Please provide a song to delete with -d")
            else:
                m_system.play_play_list(args.playlist)
        elif command == "u":
            m_system.update_tranding()
        elif command == "l":
            m_system.list_play_lists()
        elif command.startswith('save'):
            parts = command.split(maxsplit=1)
            playlist_name = parts[1] if len(parts) > 1 else ""
            m_system.save_to_playlist(playlist_name)
        elif command == "pause":
            m_system.pause_current_song()
        elif command == "play":
            m_system.play_current_song()
        elif command == "video":
            m_system.switch_to_video()
        elif command == "audio":
            m_system.switch_to_audio()
        elif command == "next":
            m_system.play_next_song()
        elif command == "exit":
            m_system.exit_tool()
        elif command == "nextall":
            m_system.display_queue()
        elif command == "previous":
            m_system.play_previous_song()
        elif command == "repeat":
            m_system.repeat_this_song()
        else:
            print("unknown command")
    except Exception as e:
        print(f"Error processing command: {str(e)}")