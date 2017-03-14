from util import *
import matplotlib.pyplot as plt
from sorting import Sorter


sorter = Sorter()
sorting_functions = {'Selection': sorter.selection_sort, 'Insertion': sorter.insertion_sort,
                     'Bubble': sorter.bubble_sort, 'Heap': sorter.heap_sort,
                     'Quick': sorter.quick_sort,'Merge': sorter.merge_sort}
results = {'Selection': [], 'Insertion': [], 'Bubble': [], 'Heap': [], 'Quick': [], 'Merge': []}
array_sizes = []


def _start():
    for i in range(0, 10):
        array_sizes.append(100 * i)
        args = get_sorted_reversed_case(100 * i, 500 * i)
        print("Test case: ", i, "\t n = ", 100 * i)
        for function in sorting_functions:
            t = measure_algorithm(args[:], sorting_functions.get(function))
            print(function, ": ", t)
            results.get(function).append(t)

    plt.xlabel("n (number of elements in array)")
    plt.ylabel("t (time taken to sort)")
    for function in sorting_functions:
        plt.plot(array_sizes, results.get(function), label=function)
    plt.legend()
    plt.show()

_start()

