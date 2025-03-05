import argparse
import shlex  
import m_system


def validate_runtime_input(command):
    runtime_parser = argparse.ArgumentParser(description="Runtime commands")
    runtime_parser.add_argument('-s', '--search', type=str, help='Search and play song')
    runtime_parser.add_argument('-p', '--playlist', type=str, help='Playlist operations')
    runtime_parser.add_argument('-a', '--audio', action='store_true', help='Audio only')
    runtime_parser.add_argument('-v', '--video', action='store_true', help='Video only')
    runtime_parser.add_argument('-ls', '--listsongs', action='store_true', help='List songs')
    runtime_parser.add_argument('-d', '--delete', type=str, help='Delete song')
    
    try:
        command_parts = shlex.split(command)
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
                m_system.delete_song(args.playlist, args.delete)
            else:
                m_system.play_play_list(args.playlist)
        elif command == "u":
            m_system.update_tranding()
        elif command == "l":
            m_system.list_play_lists()
        elif command.startswith('save'):
            playlist_name = command[len('save'):].strip()
            if len(playlist_name) > 0:
                m_system.save_to_playlist(playlist_name)
            else:
                print("No playlist name provided")
        elif command.startswith('add'):
            song = command[len('add'):].strip()
            if not song:
                print("Unknown command")
            else:
                m_system.add_to_queue(song)
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
        print(f"Error {str(e)}")
