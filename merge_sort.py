
__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "July 2018"
__email__ = "foundwonder@gmail.com"

from numpy import random as random_generator
import time
from math import *

# Generate several lists to be sorted and return a tuple
# data structure that will contain the following:
# an already sorted list, a sorted list in reverse and
# a randomly unsorted list of numbers. this will be used
# to test sorting algorithms for best, common and worst case
# scenarios !


# Generate three lists to sort
def lists_generator(end_number, list_size):
    already_sorted_list = list(range(list_size))
    random_sorted_list = random_generator.randint(end_number, size=list_size).tolist()
    reverse_sorted_list = already_sorted_list[::-1]
    return already_sorted_list, random_sorted_list, reverse_sorted_list


# Jieshu's code
# Define a function to sort and merge two lists.
def sort_merge_list_impl_j(list_1, list_2):
    list_1_index = 0
    list_2_index = 0
    result_list_index = 0
    size_list_1 = len(list_1)
    size_list_2 = len(list_2)
    temp_sorted_merged_list = [None] * (size_list_1 + size_list_2)
    size_list_temp = len(temp_sorted_merged_list)
    while result_list_index < size_list_temp:
        if list_1_index < size_list_1 and list_2_index < size_list_2:
            if list_1[list_1_index] < list_2[list_2_index]:
                temp_sorted_merged_list[result_list_index] = list_1[list_1_index]
                list_1_index = list_1_index + 1
                result_list_index = result_list_index + 1
            else:
                temp_sorted_merged_list[result_list_index] = list_2[list_2_index]
                list_2_index = list_2_index + 1
                result_list_index = result_list_index + 1
        elif list_1_index == size_list_1:
            while list_2_index < size_list_2:
                temp_sorted_merged_list[result_list_index] = list_2[list_2_index]
                result_list_index = result_list_index + 1
                list_2_index = list_2_index + 1
        elif list_2_index == size_list_2:
            while list_1_index < size_list_1:
                temp_sorted_merged_list[result_list_index] = list_1[list_1_index]
                result_list_index = result_list_index + 1
                list_1_index = list_1_index + 1
    return temp_sorted_merged_list


def sort_merge_list_impl_j_2(left_list: [], right_list: []) ->[]:

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


def merge_sort_impl_bottom_up_j(list_to_be_sorted: []) -> []:
    list_size = len(list_to_be_sorted)
    list_size_break_down = list_size
    list_break_down = list()
    for each_index in range(0, len(list_to_be_sorted)):
        list_break_down.append([list_to_be_sorted[each_index]])
    while list_size_break_down > 1:
        current_index = 0
        while current_index < list_size_break_down - 1:
            current_element = list_break_down[current_index]
            next_element = list_break_down[current_index + 1]
            sorted_element = sort_merge_list_impl_j_2(current_element, next_element)
            list_break_down[current_index] = sorted_element
            del list_break_down[current_index + 1]
            current_index = current_index + 1
            list_size_break_down = len(list_break_down)
    return list_break_down[0]


# Jieshu Wang
# a merge sort implementation using up down approach with recursion,
# which means, first, splitting the list into two lists,
# and then further splitting them, until each list has only one element,
# and then sorting and merging them back together.
def merge_sort_recursion_impl_j(list_to_be_sorted: []) ->[]:

    if len(list_to_be_sorted) == 1:
        return list_to_be_sorted

    else:
        mid_index = floor(len(list_to_be_sorted) / 2)
        left_list = list_to_be_sorted[:mid_index]
        right_list = list_to_be_sorted[mid_index:]
        left_list_sorted = merge_sort_recursion_impl_j(left_list)
        right_list_sorted = merge_sort_recursion_impl_j(right_list)
        return sort_merge_list_impl_j_2(left_list_sorted, right_list_sorted)


# Bilal El Uneis
# took the combined work done with Jieshu's recursive impl
# and attempted to minimize both the function and sorting
# loop in sort_merge_list_impl_b
def merge_sort_recursion_impl_b(list_to_sort: []) -> []:

    if len(list_to_sort) == 1:
        return list_to_sort

    else:
        list_size = len(list_to_sort)
        mid_index = floor(list_size / 2)
        left_list = list_to_sort[:mid_index]
        right_list = list_to_sort[mid_index:]
        left_list_sorted = merge_sort_recursion_impl_b(left_list)
        right_list_sorted = merge_sort_recursion_impl_b(right_list)
        return sort_merge_list_impl_b(left_list_sorted, right_list_sorted)


# Bilal El Uneis
# more minimized and easier to follow loop for sorting
# left side and right side of the list
# def sort_merge_list_impl_b(left_side: [], right_side: []) -> []:
#
#     right_index = 0
#     left_index = 0
#     result_list = list()
#
#     while left_index < len(left_side):
#
#         if right_index >= len(right_side):
#             result_list.append(left_side[left_index])
#             left_index = left_index + 1
#
#         while right_index < len(right_side):
#
#             if left_side[left_index] < right_side[right_index]:
#                 result_list.append(left_side[left_index])
#                 left_index = left_index + 1
#
#             else:
#                 result_list.append(right_side[right_index])
#                 right_index = right_index + 1
#
#     return result_list

def sort_merge_list_impl_b(left_side: [], right_side: []) -> []:

    right_index = 0
    left_index = 0
    result_list = list()

    while left_index < len(left_side):

        while right_index < len(right_side):

            if left_side[left_index] < right_side[right_index]:
                result_list.append(left_side[left_index])
                if left_index < len(left_side) - 1:
                    left_index = left_index + 1
                else:
                    result_list = result_list + list(right_side[right_index:])
                    # left_index = left_index + 1
                    break

            else:
                result_list.append(right_side[right_index])
                right_index = right_index + 1

        result_list.append(left_side[left_index])
        left_index = left_index + 1

    return result_list


def sort_merge_list(left_side, right_side):
    right_index = 0
    left_index = 0
    current_index_on_result_list = 0
    result_list = [None] * (len(left_side) + len(right_side))

    while left_index < len(left_side):

        if right_index >= len(right_side):
            result_list[current_index_on_result_list] = left_side[left_index]
            left_index = left_index + 1
            current_index_on_result_list = current_index_on_result_list + 1

        while right_index < len(right_side):

            if left_side[left_index] < right_side[right_index]:
                result_list[current_index_on_result_list] = left_side[left_index]
                left_index = left_index + 1
                current_index_on_result_list = current_index_on_result_list + 1
            else:
                result_list[current_index_on_result_list] = right_side[right_index]
                right_index = right_index + 1
                current_index_on_result_list = current_index_on_result_list + 1
    return result_list


# start of running code
if __name__ == "__main__":
    (sorted_list, random_list, reversed_list) = lists_generator(50, 5)

    print("-------------Testing Jieshu's Bottom-up Merge Sort Impl-------------")
    start_time = float(time.time() * 1000)
    result_sorted = merge_sort_impl_bottom_up_j(sorted_list)
    end_time = float(time.time() * 1000)
    print("Sorted list: in {} ms, {} was sorted to {}".format((end_time - start_time), sorted_list, result_sorted))

    start_time = float(time.time() * 1000)
    result_reversed = merge_sort_impl_bottom_up_j(reversed_list)
    end_time = float(time.time() * 1000)
    print("Reversed list: in {} ms, {} was sorted to {}".format((end_time - start_time), reversed_list, result_reversed))

    start_time = float(time.time() * 1000)
    result_random = merge_sort_impl_bottom_up_j(random_list)
    end_time = float(time.time() * 1000)
    print("Random list: in {} ms, {} was sorted to {}".format((end_time - start_time), random_list, result_random))
    print("-------------End of Testing Jieshu's Bottom-up Merge Sort Impl-------------")

    print()  # creating a new line

    print("-------------Testing Jieshu's Recursion Merge Sort Impl-------------")
    start_time = float(time.time() * 1000)
    result_sorted = merge_sort_recursion_impl_j(sorted_list)
    end_time = float(time.time() * 1000)
    print("Sorted list: in {} ms, {} was sorted to {}".format((end_time - start_time), sorted_list, result_sorted))

    start_time = float(time.time() * 1000)
    result_reversed = merge_sort_recursion_impl_j(reversed_list)
    end_time = float(time.time() * 1000)
    print("Reversed list: in {} ms, {} was sorted to {}".format((end_time - start_time), reversed_list, result_reversed))

    start_time = float(time.time() * 1000)
    result_random = merge_sort_recursion_impl_j(random_list)
    end_time = float(time.time() * 1000)
    print("Random list: in {} ms, {} was sorted to {}".format((end_time - start_time), random_list, result_random))
    print("-------------End of Testing Jieshu's Recursion Merge Sort Impl-------------")

    print()  # creating a new line

    print("-------------Testing Bilal's Recursion Merge Sort Impl-------------")
    start_time = float(time.time() * 1000)
    result_sorted = merge_sort_recursion_impl_b(sorted_list)
    end_time = float(time.time() * 1000)
    print("Sorted list: in {} ms, {} was sorted to {}".format((end_time - start_time), sorted_list, result_sorted))

    start_time = float(time.time() * 1000)
    result_reversed = merge_sort_recursion_impl_b(reversed_list)
    end_time = float(time.time() * 1000)
    print("Reversed list: in {} ms, {} was sorted to {}".format((end_time - start_time), reversed_list, result_reversed))

    start_time = float(time.time() * 1000)
    result_random = merge_sort_recursion_impl_b(random_list)
    end_time = float(time.time() * 1000)
    print("Random list: in {} ms, {} was sorted to {}".format((end_time - start_time), random_list, result_random))
    print("-------------End of Testing Bilal's Recursion Merge Sort Impl-------------")