import visualizer
import argparse
from sorting import Sorter
from util import *
"""Controls the circulation process between visualizer, sorting algorithms and plotter."""


def _get_args():
    ap = argparse.ArgumentParser(description="Sorting algorithms visualization.")
    ap.add_argument('-a', '--algorithm', type=str, help="Choose algorithm", required=True)
    args = ap.parse_args()
    return args.algorithm


algorithm = _get_args()
sorter = Sorter(enable_tracking=True)
sorting_functions = {'Selection': sorter.selection_sort, 'Insertion': sorter.insertion_sort,
                     'Bubble': sorter.bubble_sort, 'Heap': sorter.heap_sort,
                     'Quick': sorter.quick_sort, 'Merge': sorter.merge_sort}
func = sorting_functions.get(algorithm)
func(get_random_case(50, 10000))
vis = visualizer.Visualizer(sorter.track)
vis.start()
