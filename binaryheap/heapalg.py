"""**Heap queue algorithms (Priority queues)**\n
A library for the implementation of several heap algorithms.
"""

__about__ = """Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
all k, counting elements from 0.  For the sake of comparison,
non-existing elements are considered to be infinite.  The interesting
property of a heap is that a[0] is always its smallest element."""


def _parent(i):
    """Gets index of a parent of a node given the node's index."""
    return (i - 1) >> 1


def _left(i):
    """Gets index of the left child of a node."""
    return (i << 1) + 1


def _right(i):
    """Gets index of the right child of a node."""
    return (i << 1) + 2


def push(heap, item, reverse=False):
    """
    Pushes an item onto the *binaryheap*, maintaining the binaryheap invariant.
    Assumes binaryheap is already heapified.
    :type heap: list
    :param heap: Already-heapified array.

    :type item: object
    :param item: comparable.

    :type reverse: bool
    :param reverse: A boolean value indicating the reversal of the binaryheap (min_heap -> max_heap)."""
    heap.append(item)
    _sift_up(heap, len(heap) - 1, reverse)


def extract(heap, reverse=False):
    """Extracts the root item off the binaryheap, maintaining the binaryheap invariant.

    :type heap: list
    :param heap: Already-heapified array.

    :type reverse: bool
    :param reverse: A boolean value indicating the reversal of the binaryheap (min_heap -> max_heap)."""
    if len(heap) == 1:
        return heap.pop()
    ret = heap[0]
    heap[0] = heap.pop()
    heapify(heap, len(heap), reverse=reverse)
    return ret


def heapify(heap, n, i=0, reverse=False):
    """Transforms list into a binaryheap in O(n) time, if called with a certain index it assumes that subtrees are already
    heapified.

    :type heap: list
    :param heap: Already-heapified array.

    :type n: int
    :param n: Ending index of the array to be heapified.

    :type i: int
    :param i: Beginning index of the array to be heapified.

    :type reverse: bool
    :param reverse: A boolean value indicating the reversal of the binaryheap (min_heap -> max_heap)."""
    l = _left(i)
    r = _right(i)
    req = i
    if l < n and (reverse ^ (heap[l] < heap[req])):
            req = l
    if r < n and (reverse ^ (heap[r] < heap[req])):
            req = r
    if req != i:
        heap[i], heap[req] = heap[req], heap[i]
        heapify(heap, n, req, reverse)


def build_heap(heap, reverse=False):
    """Transforms a list into a binaryheap in O(n) time.

    :type heap: list
    :param heap: Already-heapified array.

    :type reverse: bool
    :param reverse: A boolean value indicating the reversal of the binaryheap (min_heap -> max_heap)."""
    i = _parent(len(heap) - 1)
    while i >= 0:
        heapify(heap, len(heap), i, reverse)
        i -= 1


def _sift_up(heap, i, reverse=False):
    if i < 0:
        pass
    parent = _parent(i)
    if parent >= 0 and (reverse ^ (heap[parent] > heap[i])):
        heap[parent], heap[i] = heap[i], heap[parent]
        _sift_up(heap, parent, reverse)
