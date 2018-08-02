__author__ = "Jieshu Wang"
__since__ = "Aug 2018"
__email__ = "foundwonder@gmail.com"

from test_data_generator import *


def selection_sort_impl_j(list_to_be_sorted: [int], visualize: bool = False) ->[int]:

    result_list = []
    initial_list = list(list_to_be_sorted)
    while len(initial_list) > 0:
        for x in initial_list:
            if min_test(x, initial_list[initial_list.index(x):]):
                initial_list.pop(initial_list.index(x))
                result_list.append(x)
                if visualize:
                    print(result_list)
                break
    return result_list


def min_test(x: int, list_to_be_tested: []) -> bool:

    for y in list_to_be_tested:
        if x > y:
            return False

    return True


# start of running code
if __name__ == "__main__":
    (sorted_list, random_list, reversed_list) = lists_generator(10, 10)
    visualization_on: bool = False
    # analyze("Bilal's Insertion Sort", selection_sort_impl_j, random_list, visualization_on)
    analyze("Jieshu's Insertion Sort", selection_sort_impl_j, sorted_list, visualization_on)
    analyze("Jieshu's Insertion Sort", selection_sort_impl_j, random_list, visualization_on)
    analyze("Jieshu's Insertion Sort", selection_sort_impl_j, reversed_list, visualization_on)