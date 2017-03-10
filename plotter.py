from random import randint
from time import time
import matplotlib.pyplot as plt
from sorting import Sorter


def get_random_case(n, rng):
    x = []
    for i in range(n):
        x.append(randint(0, rng))
    return x


def measure_algorithm(args, func):
    start = time()
    func(args)
    end = time()
    return end - start


sorting_functions = {'Selection': Sorter.selection_sort, 'Insertion': Sorter.insertion_sort,
                     'Bubble': Sorter.bubble_sort, 'Heap': Sorter.heap_sort,
                     'Quick': Sorter.quick_sort,'Merge': Sorter.merge_sort}
results = {'Selection': [], 'Insertion': [], 'Bubble': [], 'Heap': [], 'Quick': [], 'Merge': []}
array_sizes = []

for i in range(0, 10):
    array_sizes.append(100 * i)
    args = get_random_case(100 * i, 500 * i)
    print("Test case: ", i, "\t n = ", 100 * i)
    for function in sorting_functions:
        t = measure_algorithm(args.copy(), sorting_functions.get(function))
        print(function, ": ", t)
        results.get(function).append(t)

plt.xlabel("n (number of elements in array)")
plt.ylabel("t (time taken to sort)")
for function in sorting_functions:
    plt.plot(array_sizes, results.get(function), label=function)
plt.legend()
plt.show()