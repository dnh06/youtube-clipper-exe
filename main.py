import sys

def help_menu():
    print("""
Youtube Clipper EXE

Perintah:
  download <youtube_url>
  clip <video> <start> <end> <output>
  burn <video> <srt> <output>

Contoh:
  tool.exe download https://youtube.com/watch?v=xxxx
  tool.exe clip input.mp4 00:01:00 00:02:00 out.mp4
""")

def main():
    if len(sys.argv) < 2:
        help_menu()
        return

    cmd = sys.argv[1]

    if cmd == "download":
        from scripts.download_video import download_video
        download_video(sys.argv[2])

    elif cmd == "clip":
        from scripts.clip_video import clip_video
        clip_video(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

    elif cmd == "burn":
        from scripts.burn_subtitles import burn_subtitles
        burn_subtitles(sys.argv[2], sys.argv[3], sys.argv[4])

    else:
        help_menu()

if __name__ == "__main__":
    main()
