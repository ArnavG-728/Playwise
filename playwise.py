from playlist_engine_1 import PlaylistEngine
from playback_history_2 import PlaybackHistory
from song_rating_tree_3 import SongRatingBST
from song_lookup_4 import SongLookup
from playlist_sorter_5 import PlaylistSorter
from performance_analyzer_6 import PerformanceAnalyzer
from system_snapshot_7 import SystemSnapshot

class PlayWise:
    def __init__(self):
        self.playlist_engine = PlaylistEngine()
        self.playback_history = PlaybackHistory()
        self.song_rating_tree = SongRatingBST()
        self.song_lookup = SongLookup()
        self.playlist_sorter = PlaylistSorter()
        self.performance_analyzer = PerformanceAnalyzer(self.playlist_engine)
        self.system_snapshot = SystemSnapshot(
            self.playlist_engine,
            self.playback_history,
            self.song_rating_tree
        )

    def export_snapshot(self):
        return self.system_snapshot.export_snapshot()

    def analyze_performance(self):
        return self.performance_analyzer.run_analysis()

# ---------- Extended Main Test Suite -------------
if __name__ == "__main__":
    print("=" * 60)
    print("PLAYWISE COMPREHENSIVE TEST SUITE")
    print("=" * 60)

    # Initialize system
    pw = PlayWise()

    # --- TEST CASE 1: Add multiple songs (Original) ---
    print("\n--- TEST CASE 1: Basic Song Addition ---")
    songs = [
        ("Shape of You", "Ed Sheeran", 240, 5, "s1"),
        ("Blinding Lights", "The Weeknd", 200, 4, "s2"),
        ("Perfect", "Ed Sheeran", 263, 5, "s3"),
        ("Levitating", "Dua Lipa", 203, 3, "s4"),
        ("Stay", "Justin Bieber", 190, 4, "s5"),
    ]

    for title, artist, duration, rating, sid in songs:
        pw.playlist_engine.add_song(title, artist, duration)
        pw.song_rating_tree.insert_song(sid, rating, {"title": title})
        pw.song_lookup.sync_song(sid, title, {"artist": artist, "duration": duration})
    
    print(f"Added {len(songs)} songs to the system")

    # --- TEST CASE 2: Add more diverse songs ---
    print("\n--- TEST CASE 2: Diverse Genre Song Addition ---")
    diverse_songs = [
        ("Bohemian Rhapsody", "Queen", 355, 5, "s6"),
        ("Smells Like Teen Spirit", "Nirvana", 301, 4, "s7"),
        ("Billie Jean", "Michael Jackson", 294, 5, "s8"),
        ("Hotel California", "Eagles", 391, 5, "s9"),
        ("Stairway to Heaven", "Led Zeppelin", 482, 5, "s10"),
        ("Hey Jude", "The Beatles", 431, 4, "s11"),
        ("Imagine", "John Lennon", 183, 4, "s12"),
        ("Thunderstruck", "AC/DC", 292, 4, "s13"),
        ("Sweet Child O' Mine", "Guns N' Roses", 356, 4, "s14"),
        ("Purple Haze", "Jimi Hendrix", 170, 3, "s15"),
    ]

    for title, artist, duration, rating, sid in diverse_songs:
        pw.playlist_engine.add_song(title, artist, duration)
        pw.song_rating_tree.insert_song(sid, rating, {"title": title})
        pw.song_lookup.sync_song(sid, title, {"artist": artist, "duration": duration})
    
    print(f"Added {len(diverse_songs)} classic rock/pop songs")

    # --- TEST CASE 3: Add short songs ---
    print("\n--- TEST CASE 3: Short Songs Addition ---")
    short_songs = [
        ("Intro", "The xx", 90, 3, "s16"),
        ("Segue", "Radiohead", 45, 2, "s17"),
        ("Interlude", "Drake", 72, 3, "s18"),
        ("Skit", "Eminem", 38, 2, "s19"),
        ("Bridge", "Coldplay", 85, 3, "s20"),
    ]

    for title, artist, duration, rating, sid in short_songs:
        pw.playlist_engine.add_song(title, artist, duration)
        pw.song_rating_tree.insert_song(sid, rating, {"title": title})
        pw.song_lookup.sync_song(sid, title, {"artist": artist, "duration": duration})
    
    print(f"Added {len(short_songs)} short songs (under 2 minutes)")

    # --- TEST CASE 4: Add very long songs ---
    print("\n--- TEST CASE 4: Epic Length Songs Addition ---")
    long_songs = [
        ("The End", "The Doors", 676, 4, "s21"),
        ("In-A-Gadda-Da-Vida", "Iron Butterfly", 1050, 3, "s22"),
        ("Shine On You Crazy Diamond", "Pink Floyd", 810, 5, "s23"),
        ("Thick as a Brick", "Jethro Tull", 2580, 4, "s24"),
        ("Echoes", "Pink Floyd", 1434, 5, "s25"),
    ]

    for title, artist, duration, rating, sid in long_songs:
        pw.playlist_engine.add_song(title, artist, duration)
        pw.song_rating_tree.insert_song(sid, rating, {"title": title})
        pw.song_lookup.sync_song(sid, title, {"artist": artist, "duration": duration})
    
    print(f"Added {len(long_songs)} epic songs (over 10 minutes)")

    # --- TEST CASE 5: Simulate basic playback history (Original) ---
    print("\n--- TEST CASE 5: Basic Playback History ---")
    played_songs = ["Shape of You", "Blinding Lights", "Perfect", "Stay"]
    for title in played_songs:
        pw.playback_history.add_played_song(title)

    print("Recently Played Songs:")
    print(pw.playback_history.stack)

    # --- TEST CASE 6: Simulate extended playback history ---
    print("\n--- TEST CASE 6: Extended Playback History ---")
    extended_played = [
        "Bohemian Rhapsody", "Hotel California", "Stairway to Heaven",
        "Billie Jean", "Thunderstruck", "Hey Jude", "Purple Haze",
        "Sweet Child O' Mine", "Imagine", "Smells Like Teen Spirit"
    ]
    for title in extended_played:
        pw.playback_history.add_played_song(title)

    print("Extended Recently Played Songs:")
    print(pw.playback_history.stack)

    # --- TEST CASE 7: Simulate repeat listening ---
    print("\n--- TEST CASE 7: Repeat Listening Patterns ---")
    repeat_songs = ["Shape of You", "Blinding Lights", "Shape of You", "Perfect", "Shape of You"]
    for title in repeat_songs:
        pw.playback_history.add_played_song(title)

    print("After repeat listening:")
    print(pw.playback_history.stack)

    # --- TEST CASE 8: Comprehensive song lookup (Original enhanced) ---
    print("\n--- TEST CASE 8: Comprehensive Song Lookup ---")
    lookup_tests = [
        ("s3", "ID"),
        ("s10", "ID"),
        ("s25", "ID"),
        ("Stay", "Title"),
        ("Bohemian Rhapsody", "Title"),
        ("Thick as a Brick", "Title"),
        ("NonExistent", "Title"),
        ("s999", "ID"),
    ]

    for query, query_type in lookup_tests:
        if query_type == "ID":
            result = pw.song_lookup.get_by_id(query)
            print(f"Get by ID '{query}': {result}")
        else:
            result = pw.song_lookup.get_by_title(query)
            print(f"Get by Title '{query}': {result}")

    # --- TEST CASE 9: Multiple snapshot exports ---
    print("\n--- TEST CASE 9: Multiple System Snapshots ---")
    for i in range(3):
        snapshot = pw.export_snapshot()
        print(f"Snapshot {i+1}: {snapshot}")

    # --- TEST CASE 10: Sort by different criteria ---
    print("\n--- TEST CASE 10: Multiple Sorting Criteria ---")
    
    # Get current playlist for sorting tests
    current = pw.playlist_engine.head
    song_list = []
    while current:
        song_list.append({
            "title": current.title, 
            "duration": current.duration,
            "artist": getattr(current, 'artist', 'Unknown')
        })
        current = current.next

    # Sort by duration (descending)
    print("\n10a. Sorted by Duration (Descending):")
    sorted_by_duration = pw.playlist_sorter.sort_playlist(song_list, key="duration", reverse=True)
    for i, song in enumerate(sorted_by_duration[:5]):  # Show top 5
        print(f"  {i+1}. {song}")

    # Sort by duration (ascending)
    print("\n10b. Sorted by Duration (Ascending):")
    sorted_by_duration_asc = pw.playlist_sorter.sort_playlist(song_list, key="duration", reverse=False)
    for i, song in enumerate(sorted_by_duration_asc[:5]):  # Show top 5
        print(f"  {i+1}. {song}")

    # Sort by title alphabetically
    print("\n10c. Sorted by Title (Alphabetical):")
    sorted_by_title = pw.playlist_sorter.sort_playlist(song_list, key="title", reverse=False)
    for i, song in enumerate(sorted_by_title[:5]):  # Show top 5
        print(f"  {i+1}. {song}")

    # --- TEST CASE 11: Multiple performance analyses ---
    print("\n--- TEST CASE 11: Multiple Performance Analyses ---")
    for i in range(3):
        perf = pw.analyze_performance()
        print(f"Performance Analysis {i+1}: {perf}")

    # --- TEST CASE 12: Rating tree operations ---
    print("\n--- TEST CASE 12: Rating Tree Queries ---")
    rating_queries = [5, 4, 3, 2, 1]
    for rating in rating_queries:
        # Assuming the rating tree has methods to find songs by rating
        try:
            songs_by_rating = pw.song_rating_tree.find_by_rating(rating)
            print(f"Songs with rating {rating}: {songs_by_rating}")
        except AttributeError:
            print(f"Rating {rating} query method not available")

    # --- TEST CASE 13: Edge case - Empty operations ---
    print("\n--- TEST CASE 13: Edge Case Operations ---")
    
    # Create a new empty system
    pw_empty = PlayWise()
    
    print("13a. Empty system snapshot:")
    empty_snapshot = pw_empty.export_snapshot()
    print(empty_snapshot)
    
    print("13b. Empty system performance:")
    empty_perf = pw_empty.analyze_performance()
    print(empty_perf)
    
    print("13c. Empty system lookup:")
    empty_lookup = pw_empty.song_lookup.get_by_id("nonexistent")
    print(f"Empty lookup result: {empty_lookup}")

    # --- TEST CASE 14: Stress test with many songs ---
    print("\n--- TEST CASE 14: Stress Test (100 Songs) ---")
    stress_pw = PlayWise()
    
    # Generate 100 test songs
    import random
    genres = ["Pop", "Rock", "Jazz", "Classical", "Hip-Hop", "Electronic", "Country", "R&B"]
    
    for i in range(100):
        title = f"Test Song {i+1}"
        artist = f"Artist {random.choice(genres)}"
        duration = random.randint(120, 600)  # 2-10 minutes
        rating = random.randint(1, 5)
        sid = f"stress_{i+1}"
        
        stress_pw.playlist_engine.add_song(title, artist, duration)
        stress_pw.song_rating_tree.insert_song(sid, rating, {"title": title})
        stress_pw.song_lookup.sync_song(sid, title, {"artist": artist, "duration": duration})
    
    print("Added 100 songs for stress testing")
    
    # Test performance with large dataset
    stress_snapshot = stress_pw.export_snapshot()
    stress_perf = stress_pw.analyze_performance()
    print(f"Stress test snapshot: {stress_snapshot}")
    print(f"Stress test performance: {stress_perf}")

    # --- TEST CASE 15: Boundary value testing ---
    print("\n--- TEST CASE 15: Boundary Value Testing ---")
    
    boundary_songs = [
        ("Zero Duration", "Test Artist", 0, 1, "boundary_1"),  # Zero duration
        ("One Second", "Test Artist", 1, 1, "boundary_2"),    # Minimum duration
        ("Max Rating", "Test Artist", 180, 5, "boundary_3"),   # Maximum rating
        ("Min Rating", "Test Artist", 180, 1, "boundary_4"),   # Minimum rating
        ("Very Long Title " * 10, "Test Artist", 180, 3, "boundary_5"),  # Long title
        ("", "Empty Title Artist", 180, 3, "boundary_6"),     # Empty title
        ("Normal Song", "", 180, 3, "boundary_7"),            # Empty artist
    ]
    
    for title, artist, duration, rating, sid in boundary_songs:
        try:
            pw.playlist_engine.add_song(title, artist, duration)
            pw.song_rating_tree.insert_song(sid, rating, {"title": title})
            pw.song_lookup.sync_song(sid, title, {"artist": artist, "duration": duration})
            print(f"Successfully added boundary case: {title[:30]}...")
        except Exception as e:
            print(f"Error adding boundary case '{title[:30]}...': {e}")

    # --- TEST CASE 16: System state consistency ---
    print("\n--- TEST CASE 16: System State Consistency Check ---")
    
    # Test multiple operations in sequence
    consistency_songs = [
        ("Consistency Test 1", "Test Artist", 200, 4, "con_1"),
        ("Consistency Test 2", "Test Artist", 250, 3, "con_2"),
    ]
    
    for title, artist, duration, rating, sid in consistency_songs:
        pw.playlist_engine.add_song(title, artist, duration)
        pw.song_rating_tree.insert_song(sid, rating, {"title": title})
        pw.song_lookup.sync_song(sid, title, {"artist": artist, "duration": duration})
        pw.playback_history.add_played_song(title)
        
        # Check system state after each addition
        snapshot = pw.export_snapshot()
        perf = pw.analyze_performance()
        lookup = pw.song_lookup.get_by_id(sid)
        
        print(f"After adding {title}:")
        print(f"  Snapshot: {snapshot}")
        print(f"  Performance: {perf}")
        print(f"  Lookup: {lookup}")

    print("\n" + "=" * 60)
    print("ALL TEST CASES COMPLETED")
    print("=" * 60)