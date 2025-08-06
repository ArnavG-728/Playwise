class SongNode:
    """Represents a single song in the doubly linked list."""
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.prev = None
        self.next = None

class PlaylistEngine:
    """
    Manages the playlist using a doubly linked list data structure.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_song(self, title, artist, duration):
        """Adds a new song to the end of the playlist."""
        new_node = SongNode(title, artist, duration)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def delete_song(self, index):
        """Deletes a song at a given index."""
        if index < 0 or index >= self.size:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        self.size -= 1

    def move_song(self, from_index, to_index):
        """Moves a song from one index to another."""
        if from_index == to_index or from_index < 0 or to_index < 0 or from_index >= self.size or to_index >= self.size:
            return

        # Isolate the song node to be moved
        current = self.head
        for _ in range(from_index):
            current = current.next

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

        # Find the insertion point
        target = self.head
        for _ in range(to_index):
            target = target.next

        # Insert the song node at the new position
        if target.prev:
            target.prev.next = current
            current.prev = target.prev
        else:
            self.head = current
            current.prev = None

        current.next = target
        target.prev = current

    def reverse_playlist(self):
        """Reverses the order of the playlist."""
        current = self.head
        prev_node = None
        while current:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            prev_node = current
            current = next_node
        self.head, self.tail = self.tail, self.head