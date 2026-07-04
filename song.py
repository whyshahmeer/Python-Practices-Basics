class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def playlist(self):
        return f"{self.title} by {self.artist}"


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        if isinstance(song, Song):
            self.songs.append(song)
        else:
            raise TypeError("Only Song objects can be added.")

    def remove_song(self, title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                self.songs.remove(song)
                return True
        return False

    def get_artist_songs(self, artist_name):
        return [
            song
            for song in self.songs
            if song.artist.lower() == artist_name.lower()
        ]


playlist = Playlist()

for i in range(2):
    print(f"\nEnter Song {i + 1}")

    title = input("Title: ")
    artist = input("Artist: ")

    playlist.add_song(Song(title, artist))


print("\nAll Songs:")
for song in playlist.songs:
    print(song.playlist())

artist_name = input("\nEnter artist name to search: ")

print(f"\nSongs by {artist_name}:")
for song in playlist.get_artist_songs(artist_name):
    print(song.playlist())

remove = input("\nEnter song title to remove: ")
playlist.remove_song(remove)

print("\nPlaylist After Removing:")
for song in playlist.songs:
    print(song.playlist())




