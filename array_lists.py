class Album:
    def __init__(self, albumName, numberOfSongs, albumArtist):
        self.albumName = albumName
        self.numberOfSongs = numberOfSongs
        self.albumArtist = albumArtist

    def __str__(self):
        return f"({self.albumName}, {self.albumArtist}, {self.numberOfSongs})"
    

albums1 = [
    ("Album 1", "Artist 1", 12),
    ("Album 2", "Artist 2", 8),
    ("Album 3", "Artist 3", 10),
    ("Album 4", "Artist 4", 15),
    ("Album 5", "Artist 5", 11)
]

# Sort the list by numberOfSongs
sorted_albums = sorted(albums1, key=lambda album: album[2])

# Print the sorted list
for album in sorted_albums:
    print(album)
    
    
albums1 = [
    ("Album 1", "Juice Wrld ", 12),
    ("Album 20", "Centarl Cee", 8),
    ("Album 30", "Lii baby ", 10),
    ("Album 40", "Kanye west ", 15),
    ("Album 50", "Drake ", 11)
]
       
# Swap elements at positions 1 and 2
albums1[1], albums1[2] = albums1[2], albums1[1]

# Print the updated list
for album in albums1:
    print(album)


# Adding albums to the list
albums2 = [("Album 1", "Michael Jackson ", 1),
    ("Album 100", "Celine Dion", 2),
    ("Album 200", "Phil Collins", 3),
    ("Album 300", "Marvin Gaye", 4),
    ("Album 400", "Bob Marley", 5),
    ("Dark Side of the Moon", "Pink Floyd", 9),
    ("Oops!... I Did It Again", "Britney Spears", 16),
]

# Printing the list
for album in albums2:
    print(album)

# Copy albums from albums1 to albums2
albums2.extend(albums1)

# Print albums2
for album in albums2:
    print(album)


# Sort the list by numberOfSongs
sorted_albums = sorted(albums2, key=lambda album: album[2])

# Print the sorted list
for album in sorted_albums:
    print(album)
    

# Search for "Dark Side of the Moon" album and print its index
for index, album in enumerate(albums2):
    if album[0] == "Dark Side of the Moon":
        print("Index of 'Dark Side of the Moon' album:", index)
        break
else:
    print("'Dark Side of the Moon' album not found in the list.")