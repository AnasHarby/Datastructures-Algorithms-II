from algobserver import AlgorithmObserver
from sorting import Sorter
import visualizer


sorting_functions = {'Selection': Sorter.selection_sort, 'Insertion': Sorter.insertion_sort,
                     'Bubble': Sorter.bubble_sort, 'Heap': Sorter.heap_sort,
                     'Quick': Sorter.quick_sort,'Merge': Sorter.merge_sort}
sorter = Sorter()
sorter.attach_observer(AlgorithmObserver)
visualizer.start()
print("x")