playlist = ["song1", "song2", "song3"]
i=input('enter the intro song')
playlist.insert(0,i)
playlist.remove('song2')
o=input('enter the outro song')
playlist.insert(-1,i)
print(playlist)
