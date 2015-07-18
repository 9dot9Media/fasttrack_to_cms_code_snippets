from mutagen.easymp3 import EasyMP3
mp3 = EasyMP3("audio_file.mp3")
print(mp3.tags['album'])