class SystemSnapshot:
    """
    Captures a snapshot of key data from various parts of the system.
    """
    def __init__(self, playlist_engine, playback_history, rating_tree):
        self.playlist_engine = playlist_engine
        self.playback_history = playback_history
        self.rating_tree = rating_tree

    def export_snapshot(self):
        """
        Creates and returns a dictionary containing a summary of system state.
        """
        return {
            "top_5_longest_songs": self.get_top_5_longest_songs(),
            "recently_played": self.playback_history.stack[-5:],
            "rating_counts": self.get_rating_counts()
        }

    def get_top_5_longest_songs(self):
        """
        Retrieves the top 5 longest songs from the playlist.
        O(n log n) due to sorting, where n is the number of songs.
        """
        current = self.playlist_engine.head
        songs = []
        while current:
            songs.append({"title": current.title, "duration": current.duration})
            current = current.next
        songs.sort(key=lambda x: x["duration"], reverse=True)
        return songs[:5]

    def get_rating_counts(self):
        """
        Counts the number of songs for each rating in the rating tree.
        O(r) time, where r is the number of unique ratings (at most 5).
        """
        counts = {}
        def traverse(node):
            if node:
                counts[node.rating] = len(node.songs)
                traverse(node.left)
                traverse(node.right)
        traverse(self.rating_tree.root)
        return counts