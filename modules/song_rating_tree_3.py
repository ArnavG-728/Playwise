# song_rating_tree.py - Binary Search Tree for Song Ratings

class RatingNode:
    def __init__(self, rating):
        self.rating = rating
        self.songs = []  # Each element: {"id": song_id, "metadata": {...}}
        self.left = None
        self.right = None

class SongRatingBST:
    def __init__(self):
        self.root = None

    # O(log n) average, O(n) worst-case
    def insert_song(self, song_id, rating, metadata):
        def insert(node):
            if not node:
                new_node = RatingNode(rating)
                new_node.songs.append({"id": song_id, "metadata": metadata})
                return new_node
            if rating < node.rating:
                node.left = insert(node.left)
            elif rating > node.rating:
                node.right = insert(node.right)
            else:
                node.songs.append({"id": song_id, "metadata": metadata})
            return node

        self.root = insert(self.root)

    # O(log n) average, O(n) worst-case
    def search_by_rating(self, rating):
        current = self.root
        while current:
            if rating < current.rating:
                current = current.left
            elif rating > current.rating:
                current = current.right
            else:
                return current.songs
        return []

    # O(n) time, O(1) space
    def delete_song(self, song_id):
        def delete_in_node(node):
            if not node:
                return
            node.songs = [s for s in node.songs if s["id"] != song_id]
            delete_in_node(node.left)
            delete_in_node(node.right)

        delete_in_node(self.root)
