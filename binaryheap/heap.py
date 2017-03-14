from queue import PriorityQueue
from binaryheap import heapalg


class Heap(PriorityQueue):
    """A binary heap that implements a Priority Queue, default is a Min Heap."""
    def __init__(self, reverse=False, array=[]):
        """Constructs a new heap.

        :type reverse: reverses the heap to convert it to a Max Heap.
        :param reverse"""
        super().__init__()
        self.array = array[:]
        self.reverse = reverse
        self._build_heap()

    def _build_heap(self):
        heapalg.build_heap(self.array, self.reverse)

    def qsize(self):
        """Returns current size of the heap."""
        return len(self.array)

    def empty(self):
        """Checks if the heap is empty."""
        return self.qsize() == 0

    def push(self, *items):
        """Pushes a new item to the heap keeping the heap invariant."""
        for item in list(items):
            heapalg.push(self.array, item, self.reverse)

    def pop(self):
        """Pops the root item from the heap keeping the heap invariant."""
        return heapalg.extract(self.array, self.reverse)

