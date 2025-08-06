# play_duration_visualizer_9.py

class PlayDurationVisualizer:
    """
    Analyzes and visualizes playlist duration data from the PlaylistEngine.
    """
    def __init__(self, playlist_engine):
        # The PlaylistEngine instance to be analyzed.
        self.engine = playlist_engine

    # O(n) time, O(1) space, where n is the number of songs.
    def get_duration_summary(self):
        """
        Calculates and returns a summary of the playlist's total playtime,
        as well as the shortest and longest songs.
        """
        current = self.engine.head
        if not current:
            # Return an empty summary if the playlist is empty.
            return {"total": 0, "longest": None, "shortest": None}

        total = 0
        min_song = {"title": current.title, "duration": current.duration}
        max_song = {"title": current.title, "duration": current.duration}

        while current:
            # Iterate through the linked list to calculate totals and find min/max.
            total += current.duration
            if current.duration < min_song["duration"]:
                min_song = {"title": current.title, "duration": current.duration}
            if current.duration > max_song["duration"]:
                max_song = {"title": current.title, "duration": current.duration}
            current = current.next

        return {
            "total_playtime_sec": total,
            "shortest_song": min_song,
            "longest_song": max_song
        }