class SongLookup:
    def __init__(self):
        self.song_by_id = {}
        self.song_by_title = {}

    def sync_song(self, song_id, title, metadata):
        self.song_by_id[song_id] = metadata
        self.song_by_title[title] = metadata

    def get_by_id(self, song_id):
        return self.song_by_id.get(song_id)

    def get_by_title(self, title):
        return self.song_by_title.get(title)
