# playlist_sorter_5.py - Sort Playlist using Merge Sort

class PlaylistSorter:
    """
    Sorts a list of songs using the Merge Sort algorithm.
    """
    # O(n log n) time, O(n) space complexity
    def merge_sort(self, songs, key, reverse=False):
        """
        Recursively sorts a list of songs by a given key.
        """
        # Base case for recursion: a list of one or zero elements is already sorted.
        if len(songs) <= 1:
            return songs

        # Divide the list into two halves.
        mid = len(songs) // 2
        left = self.merge_sort(songs[:mid], key, reverse)
        right = self.merge_sort(songs[mid:], key, reverse)

        # Conquer: merge the sorted halves.
        return self._merge(left, right, key, reverse)

    def _merge(self, left, right, key, reverse):
        """
        Merges two sorted sublists into a single sorted list.
        """
        result = []
        i = j = 0

        # Compare elements from both lists and add the smaller/larger to the result.
        while i < len(left) and j < len(right):
            if (left[i][key] < right[j][key] and not reverse) or (left[i][key] > right[j][key] and reverse):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Append any remaining elements.
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Entry point for the sorting process.
    def sort_playlist(self, songs, key="title", reverse=False):
        """
        Public method to sort the playlist. Defaults to sorting by title.
        """
        return self.merge_sort(songs, key, reverse)