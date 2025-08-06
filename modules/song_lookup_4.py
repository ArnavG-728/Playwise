class SongLookup:
    """
    Provides fast lookup for songs using hash maps (dictionaries).
    """
    def __init__(self):
        # Hash map for O(1) lookup by song ID.
        self.song_by_id = {}
        # Hash map for O(1) lookup by song title.
        self.song_by_title = {}

    # O(1) average time complexity for insertion.
    def sync_song(self, song_id, title, metadata):
        """
        Adds or updates a song's metadata in both lookup dictionaries.
        """
        self.song_by_id[song_id] = metadata
        self.song_by_title[title] = metadata

    # O(1) average time complexity for lookup.
    def get_by_id(self, song_id):
        """
        Retrieves song metadata using its unique ID.
        """
        return self.song_by_id.get(song_id)

    # O(1) average time complexity for lookup.
    def get_by_title(self, title):
        """
        Retrieves song metadata using its title.
        """
        return self.song_by_title.get(title)