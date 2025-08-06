# performance_analyzer_6.py - Analyze Time and Space Complexity

import time
import tracemalloc

class PerformanceAnalyzer:
    """
    Measures the time and space complexity of operations on the playlist.
    """
    def __init__(self, playlist_engine):
        # The PlaylistEngine instance whose performance is to be analyzed.
        self.engine = playlist_engine

    def run_analysis(self):
        """
        Runs a performance analysis on a specific operation (e.g., reversing the playlist).
        The time complexity of this method is determined by the analyzed operation (O(n) for reverse_playlist).
        The space complexity is O(1) as it only stores a few variables for measurement.
        """
        tracemalloc.start()
        start_time = time.time()

        self.engine.reverse_playlist()  # Example operation to analyze

        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return {
            "execution_time_sec": round(end_time - start_time, 6),
            "current_memory_kb": round(current / 1024, 2),
            "peak_memory_kb": round(peak / 1024, 2)
        }