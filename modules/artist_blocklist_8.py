# artist_blocklist_8.py

class ArtistBlocklist:
    """
    Manages a list of blocked artists using a hash set for efficient operations.
    """
    def __init__(self):
        # A set to store blocked artist names for O(1) average time complexity.
        self.blocked_artists = set()

    # O(1) average time complexity due to hash set insertion.
    def block_artist(self, artist_name):
        """Adds an artist to the blocklist."""
        self.blocked_artists.add(artist_name.lower())

    # O(1) average time complexity due to hash set removal.
    def unblock_artist(self, artist_name):
        """Removes an artist from the blocklist."""
        self.blocked_artists.discard(artist_name.lower())

    # O(1) average time complexity due to hash set lookup.
    def is_blocked(self, artist_name):
        """Checks if an artist is in the blocklist."""
        return artist_name.lower() in self.blocked_artists

    # O(n) time complexity to convert the set to a list, where n is the number of blocked artists.
    def get_all_blocked(self):
        """Returns a list of all blocked artists."""
        return list(self.blocked_artists)