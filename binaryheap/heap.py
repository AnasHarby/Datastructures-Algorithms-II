from queue import PriorityQueue
from binaryheap import heapalg


class Heap(PriorityQueue):
    """A """
    def __init__(self, reverse=False, array=[]):
        super().__init__()
        self.array = array.copy()
        self.reverse = reverse
        self._build_heap()

    def _build_heap(self):
        heapalg.build_heap(self.array, self.reverse)

    def qsize(self):
        return len(self.array)

    def empty(self):
        return self.qsize() == 0

    def push(self, *items):
        for item in list(items):
            heapalg.push(self.array, item, self.reverse)

    def pop(self):
        return heapalg.extract(self.array, self.reverse)

