import random

def dj_shuffle(songs):
    shuffled_songs = songs.copy()
    random.shuffle(shuffled_songs)
    return shuffled_songs
songs = [
    "Shape of You - Ed Sheeran",
    "Blinding Lights - The Weeknd",
    "Levitating - Dua Lipa",
    "Perfect - Ed Sheeran",
    "Senorita - Shawn Mendes, Camila Cabello",
    "Believer - Imagine Dragons",
    "Girls Like You - Maroon 5",
    "Stay - The Kid LAROI, Justin Bieber",
    "Counting Stars - OneRepublic",
    "Someone Like You - Adele"
]

print(dj_shuffle(songs))
