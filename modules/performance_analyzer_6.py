# performance_analyzer.py - Analyze Time and Space Complexity

import time
import tracemalloc

class PerformanceAnalyzer:
    def __init__(self, playlist_engine):
        self.engine = playlist_engine

    def run_analysis(self):
        tracemalloc.start()
        start_time = time.time()

        self.engine.reverse_playlist()  # Example operation

        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return {
            "execution_time_sec": round(end_time - start_time, 6),
            "current_memory_kb": round(current / 1024, 2),
            "peak_memory_kb": round(peak / 1024, 2)
        }
