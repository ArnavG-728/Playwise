# playback_history.py - Stack for Playback History

class PlaybackHistory:
    """
    Manages the history of played songs using a stack (LIFO principle).
    """
    def __init__(self):
        # A list acting as a stack to store played songs.
        self.stack = []

    # O(1) time and space complexity for appending to a list.
    def add_played_song(self, song):
        """
        Adds a song to the playback history stack.
        """
        self.stack.append(song)

    # O(1) time and space complexity for popping from a list.
    def undo_last_play(self):
        """
        Removes and returns the most recently played song.
        Returns None if the stack is empty.
        """
        if self.stack:
            return self.stack.pop()
        return None