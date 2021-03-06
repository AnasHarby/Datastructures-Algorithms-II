import random
from queue import Queue

from binaryheap import heapalg


class Sorter:
    """Sorting utility class that holds multiple sorting algorithms and an optional tracker."""
    def __init__(self, enable_tracking=False):
        """Constructs a new sorter.

        :type enable_tracking: bool
        :param enable_tracking: Enables tracking for the sorting algorithms, making each
        and every sorting algorithm able to return a queue holding the tracking criteria.
        """
        self.track = Queue()
        self.enable_tracking = enable_tracking

    def heap_sort(self, args, reverse=False):
        """Heap sorting algorithm, O(n log n)"""
        heapalg.build_heap(args, not reverse)
        for i in reversed(range(len(args))):
            args[0], args[i] = args[i], args[0]
            heapalg.heapify(args, i, reverse=not reverse)
            if self.enable_tracking:
                self.track.put(args[:])

    def merge_sort(self, args, reverse=False):
        """Merge sorting algorithm, O(n log n)"""
        self._merge_sort(args, 0, len(args) - 1, reverse)

    def _merge_sort(self, args, l, r, reverse):
        if l < r:
            m = (l + (r - 1)) // 2
            self._merge_sort(args, l, m, reverse)
            self._merge_sort(args, m + 1, r, reverse)
            self._merge(args, l, m, r, reverse)
            if self.enable_tracking:
                self.track.put(args[:])
        pass

    def _merge(self, args, l, m, r, reverse):
        n1 = m - l + 1
        n2 = r - m
        left_arr = []
        right_arr = []
        for i in range(0, n1):
            left_arr.append(args[l + i])
        for j in range(0, n2):
            right_arr.append(args[m + 1 + j])
        if reverse:
            right_arr.append(float("-inf"))
            left_arr.append(float("-inf"))
        else:
            right_arr.append(float("inf"))
            left_arr.append(float("inf"))
        i = 0
        j = 0
        k = l
        while i < n1 or j < n2:
            if reverse ^ (left_arr[i] <= right_arr[j]):
                args[k] = left_arr[i]
                i += 1
            else:
                args[k] = right_arr[j]
                j += 1
            k += 1

    def quick_sort(self, args, reverse=False, random=False):
        """Quick sorting algorithm, O (n log n).

        :type random: bool
        :param random: Choosing random partitioning algorithm (Hoare) instead of
        standard random partitioning algorithm (Lomuto).
        """
        if not random:
            self._quick_sort(args, 0, len(args) - 1, reverse)
        else:
            self._quick_sort_random(args, 0, len(args) - 1, reverse)

    def _quick_sort(self, args, p, r, reverse):
        if self.enable_tracking:
            self.track.put(args[:])
        if p < r:
            q = self._partition(args, p, r, reverse)
            self._quick_sort(args, p, q - 1, reverse)
            self._quick_sort(args, q + 1, r, reverse)

    def _quick_sort_random(self, args, p, r, reverse):
        if self.enable_tracking:
            self.track.put(args[:])
        if p < r:
            q = self._random_partition(args, p, r, reverse)
            self._quick_sort_random(args, p, q - 1, reverse)
            self._quick_sort_random(args, q + 1, r, reverse)

    def _partition(self, args, p, r, reverse):
        x = args[r]
        i = p - 1
        for j in range(p, r):
            if reverse ^ (args[j] <= x):
                i += 1
                args[i], args[j] = args[j], args[i]
        i += 1
        args[i], args[r] = args[r], args[i]
        return i

    def _random_partition(self, args, p, r, reverse):
        q = random.randint(p, r)
        args[r], args[q] = args[q], args[r]
        return self._partition(args, p, r, reverse)

    def selection_sort(self, args, reverse=False):
        """Selection sorting algorithm O(n^2)."""
        for i in range(len(args)):
            req_index = i
            for j in range(i + 1, len(args)):
                if reverse ^ (args[req_index] > args[j]):
                    req_index = j
            args[i], args[req_index] = args[req_index], args[i]
            if self.enable_tracking:
                self.track.put(args[:])

    def bubble_sort(self, args, reverse=False):
        """Bubble sorting algorithm O(n^2)."""
        for i in range(len(args)):
            found = False
            for j in range(len(args) - 1 - i):
                if reverse ^ (args[j] > args[j + 1]):
                    found = True
                    args[j], args[j + 1] = args[j + 1], args[j]
                    if self.enable_tracking:
                        self.track.put(args[:])
            if not found:
                pass

    def insertion_sort(self, args, reverse=False):
        """Insertion sorting algorithm O(n^2)."""
        for i in range(1, len(args)):
            temp = args[i]
            j = i - 1
            while j >= 0 and (reverse ^ (temp < args[j])):
                args[j + 1] = args[j]
                if self.enable_tracking:
                    self.track.put(args[:])
                j -= 1
            args[j + 1] = temp
            if self.enable_tracking:
                self.track.put(args[:])
