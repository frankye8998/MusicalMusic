import MusicalMusic
import getpass

username = input("Username: ")
password = getpass.getpass()

MyInstance = MusicalMusic.MusicalMusic(username, password)

query = input("What's your favourite song? ")
results = MusicalMusic.search(query)
song = results[0]

id = song["id"]
title = song["title"]
instruments = song["instruments"]
duration = song["duration"]

MyInstance.download(id, "song.mp3")

print(f'''Title: {title}
Duration: {duration}
Instruments: {instruments}
''')
