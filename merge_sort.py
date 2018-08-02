
__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "July 2018"
__email__ = "foundwonder@gmail.com"

from math import *
from test_data_generator import *


def sort_merge_list(left_list: [int], right_list: [int]) ->[int]:

    left_index = 0
    right_index = 0
    result_list = list()

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            result_list.append(left_list[left_index])
            left_index = left_index + 1
        else:
            result_list.append(right_list[right_index])
            right_index = right_index + 1

    if left_index == len(left_list):
        result_list = result_list + right_list[right_index:]
    if right_index == len(right_list):
        result_list = result_list + left_list[left_index:]

    return result_list


# Jieshu Wang
# a merge sort implementation using bottom up approach,
# which means, first, breaking the list into lists
# with one element, and then merging two adjacent lists.


def merge_sort_bottom_up(list_to_be_sorted: [int], visualize: bool = False) -> [int]:
    list_size = len(list_to_be_sorted)
    list_size_break_down = list_size
    list_break_down = list()
    for each_index in range(0, len(list_to_be_sorted)):
        list_break_down.append([list_to_be_sorted[each_index]])
    if visualize:
        print(list_break_down)
    while list_size_break_down > 1:
        current_index = 0
        while current_index < list_size_break_down - 1:
            current_element = list_break_down[current_index]
            next_element = list_break_down[current_index + 1]
            sorted_element = sort_merge_list(current_element, next_element)
            list_break_down[current_index] = sorted_element
            del list_break_down[current_index + 1]
            current_index = current_index + 1
            list_size_break_down = len(list_break_down)
            if visualize:
                print(list_break_down)
    return list_break_down[0]


# Jieshu Wang
# a merge sort implementation using up down approach with recursion,
# which means, first, splitting the list into two lists,
# and then further splitting them, until each list has only one element,
# and then sorting and merging them back together.
def merge_sort_recursion(list_to_be_sorted: [int], visualize: bool = False) ->[int]:

    if visualize and len(list_to_be_sorted) > 1:
        print("list {} is broken down to".format(list_to_be_sorted))

    if len(list_to_be_sorted) == 1:
        return list_to_be_sorted

    else:
        mid_index = floor(len(list_to_be_sorted) / 2)
        left_list = list_to_be_sorted[:mid_index]
        right_list = list_to_be_sorted[mid_index:]
        if visualize:
            print("left list {} and right list {}".format(left_list, right_list))
            print("recurse on the left list {}".format(left_list))
        left_list_sorted = merge_sort_recursion(left_list, visualize)
        if visualize:
            print("recurse on the right list {}".format(right_list))
        right_list_sorted = merge_sort_recursion(right_list, visualize)
        result_after_sort = sort_merge_list(left_list_sorted, right_list_sorted)
        if visualize:
            print("sort them respectively to {} and {}".format(left_list_sorted, right_list_sorted))
            print("combine and sort them to {}".format(result_after_sort))

        return result_after_sort


# start of running code
if __name__ == "__main__":
    (sorted_list, random_list, reversed_list) = lists_generator(20, 5)
    visualization_on: bool = True
    # analyze("Bilal's merge Sort", merge_sort_recursion_impl_j, random_list, visualization_on)
    analyze("Recursion merge Sort", merge_sort_recursion, random_list, visualization_on)
    analyze("Jieshu's bottom up merge Sort", merge_sort_bottom_up, random_list, visualization_on)
