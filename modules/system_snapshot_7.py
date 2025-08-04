class SystemSnapshot:
    def __init__(self, playlist_engine, playback_history, rating_tree):
        self.playlist_engine = playlist_engine
        self.playback_history = playback_history
        self.rating_tree = rating_tree

    def export_snapshot(self):
        return {
            "top_5_longest_songs": self.get_top_5_longest_songs(),
            "recently_played": self.playback_history.stack[-5:],
            "rating_counts": self.get_rating_counts()
        }

    def get_top_5_longest_songs(self):
        current = self.playlist_engine.head
        songs = []
        while current:
            songs.append({"title": current.title, "duration": current.duration})
            current = current.next
        songs.sort(key=lambda x: x["duration"], reverse=True)
        return songs[:5]

    def get_rating_counts(self):
        counts = {}
        def traverse(node):
            if node:
                counts[node.rating] = len(node.songs)
                traverse(node.left)
                traverse(node.right)
        traverse(self.rating_tree.root)
        return counts
