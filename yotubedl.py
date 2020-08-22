from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=XCZKEhGsfX0'])
    info_dict = ydl.extract_info("https://www.youtube.com/watch?v=XCZKEhGsfX0", download=False)
    print(info_dict.get('title', None))
