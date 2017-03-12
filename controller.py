import visualizer
import argparse
from sorting import Sorter
from random import randint


def get_random_case(n, rng):
    x = []
    for i in range(n):
        x.append(randint(0, rng))
    return x


def get_args():
    ap = argparse.ArgumentParser(description="Sorting algorithms visualization.")
    ap.add_argument('-a', '--algorithm', type=str, help="Choose algorithm", required=True)
    args = ap.parse_args()
    return args.algorithm


algorithm = get_args()
sorter = Sorter()
sorting_functions = {'Selection': sorter.selection_sort, 'Insertion': sorter.insertion_sort,
                     'Bubble': sorter.bubble_sort, 'Heap': sorter.heap_sort,
                     'Quick': sorter.quick_sort, 'Merge': sorter.merge_sort}
func = sorting_functions.get(algorithm)
func(get_random_case(50, 10000))
vis = visualizer.Visualizer(sorter.track)
vis.start()