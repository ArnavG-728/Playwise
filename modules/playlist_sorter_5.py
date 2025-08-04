# playlist_sorter.py - Sort Playlist using Merge Sort

class PlaylistSorter:
    # O(n log n) time, O(n) space
    def merge_sort(self, songs, key, reverse=False):
        if len(songs) <= 1:
            return songs

        mid = len(songs) // 2
        left = self.merge_sort(songs[:mid], key, reverse)
        right = self.merge_sort(songs[mid:], key, reverse)

        return self._merge(left, right, key, reverse)

    def _merge(self, left, right, key, reverse):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if (left[i][key] < right[j][key] and not reverse) or (left[i][key] > right[j][key] and reverse):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Entry point
    def sort_playlist(self, songs, key="title", reverse=False):
        return self.merge_sort(songs, key, reverse)
