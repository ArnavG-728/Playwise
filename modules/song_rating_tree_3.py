# song_rating_tree.py - Binary Search Tree for Song Ratings

class RatingNode:
    """Represents a node in the BST, holding songs of a specific rating."""
    def __init__(self, rating):
        self.rating = rating
        self.songs = []  # A list of songs with this rating.
        self.left = None
        self.right = None

class SongRatingBST:
    """
    A Binary Search Tree (BST) to efficiently store and retrieve songs by their rating.
    The tree structure is based on the rating value.
    """
    def __init__(self):
        self.root = None

    # O(log n) on average, O(n) in the worst-case (unbalanced tree), where n is the number of unique ratings.
    def insert_song(self, song_id, rating, metadata):
        """
        Inserts a new song into the BST based on its rating.
        If a node for the rating exists, the song is added to that node's list.
        """
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

    # O(log n) on average, O(n) in the worst-case, where n is the number of unique ratings.
    def search_by_rating(self, rating):
        """
        Searches for and returns all songs that have a specific rating.
        """
        current = self.root
        while current:
            if rating < current.rating:
                current = current.left
            elif rating > current.rating:
                current = current.right
            else:
                return current.songs
        return []

    # O(s) where s is the total number of songs in the tree.
    # This is not a typical BST deletion; it's a full traversal to find and remove a specific song ID.
    def delete_song(self, song_id):
        """
        Deletes a song by its ID, traversing the entire tree.
        """
        def delete_in_node(node):
            if not node:
                return
            node.songs = [s for s in node.songs if s["id"] != song_id]
            delete_in_node(node.left)
            delete_in_node(node.right)

        delete_in_node(self.root)