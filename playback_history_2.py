# playback_history.py - Stack for Playback History

class PlaybackHistory:
    def __init__(self):
        self.stack = []

    # O(1) time, O(1) space
    def add_played_song(self, song):
        self.stack.append(song)

    # O(1) time, O(1) space
    def undo_last_play(self):
        if self.stack:
            return self.stack.pop()
        return None
