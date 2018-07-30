
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
def lists_generator(end_number, list_size):
    already_sorted_list = list(range(list_size))
    random_sorted_list = random_generator.randint(end_number, size=list_size).tolist()
    reverse_sorted_list = already_sorted_list[::-1]
    return already_sorted_list, random_sorted_list, reverse_sorted_list


# define a function that compare and merge two lists.
def list_compare_merge(list_1, list_2):
    current_index_list_1 = 0
    current_index_list_2 = 0
    current_index_temp_list = 0
    size_list_1 = len(list_1)
    size_list_2 = len(list_2)
    temp_sorted_merged_list = [None] * (size_list_1 + size_list_2)
    size_list_temp = len(temp_sorted_merged_list)
    while current_index_temp_list < size_list_temp:
        if current_index_list_1 < size_list_1 and current_index_list_2 < size_list_2:
            if list_1[current_index_list_1] < list_2[current_index_list_2]:
                temp_sorted_merged_list[current_index_temp_list] = list_1[current_index_list_1]
                current_index_list_1 = current_index_list_1 + 1
                current_index_temp_list = current_index_temp_list + 1
            else:
                temp_sorted_merged_list[current_index_temp_list] = list_2[current_index_list_2]
                current_index_list_2 = current_index_list_2 + 1
                current_index_temp_list = current_index_temp_list + 1
        elif current_index_list_1 == size_list_1:
            while current_index_list_2 < size_list_2:
                temp_sorted_merged_list[current_index_temp_list] = list_2[current_index_list_2]
                current_index_temp_list = current_index_temp_list + 1
                current_index_list_2 = current_index_list_2 + 1
        elif current_index_list_2 == size_list_2:
            while current_index_list_1 < size_list_1:
                temp_sorted_merged_list[current_index_temp_list] = list_1[current_index_list_1]
                current_index_temp_list = current_index_temp_list + 1
                current_index_list_1 = current_index_list_1 + 1
    # print(temp_sorted_merged_list)
    return temp_sorted_merged_list


def merge_sort_impl_j(list_to_be_sorted):

    list_size = len(list_to_be_sorted)
    list_size_break_down = list_size
    sorted_list = [None]
    # Create a list that consists of lists, each of which only has one element.
    list_break_down = [None] * list_size_break_down
    for each_index in range(0,list_size_break_down):
        list_break_down[each_index] = [list_to_be_sorted[each_index]]
    while list_size_break_down > 1:
        current_index = 0
        while current_index < list_size_break_down - 1:
            current_element = list_break_down[current_index]
            next_element = list_break_down[current_index + 1]
            sorted_element = list_compare_merge(current_element, next_element)
            list_break_down[current_index] = sorted_element
            del list_break_down[current_index + 1]
            current_index = current_index + 1
            list_size_break_down = len(list_break_down)

    sorted_list = list_break_down[0]
    return sorted_list

# Try using recursion to write merge sort
def list_compare_merge_recursion(list_1, list_2):
    current_index_list_1 = 0
    current_index_list_2 = 0
    current_index_temp_list = 0
    size_list_1 = len(list_1)
    size_list_2 = len(list_2)
    temp_sorted_merged_list = [None] * (size_list_1 + size_list_2)
    size_list_temp = len(temp_sorted_merged_list)

    while current_index_temp_list < size_list_temp:
        if current_index_list_1 < size_list_1 and current_index_list_2 < size_list_2:
            if list_1[current_index_list_1] < list_2[current_index_list_2]:
                temp_sorted_merged_list[current_index_temp_list] = list_1[current_index_list_1]
                current_index_list_1 = current_index_list_1 + 1
                current_index_temp_list = current_index_temp_list + 1
            else:
                temp_sorted_merged_list[current_index_temp_list] = list_2[current_index_list_2]
                current_index_list_2 = current_index_list_2 + 1
                current_index_temp_list = current_index_temp_list + 1
        elif current_index_list_1 == size_list_1:
            while current_index_list_2 < size_list_2:
                temp_sorted_merged_list[current_index_temp_list] = list_2[current_index_list_2]
                current_index_temp_list = current_index_temp_list + 1
                current_index_list_2 = current_index_list_2 + 1
        elif current_index_list_2 == size_list_2:
            while current_index_list_1 < size_list_1:
                temp_sorted_merged_list[current_index_temp_list] = list_1[current_index_list_1]
                current_index_temp_list = current_index_temp_list + 1
                current_index_list_1 = current_index_list_1 + 1
    # print(temp_sorted_merged_list)
    return temp_sorted_merged_list

def merge_sort_impl_recursion(list_to_be_sorted):

    list_size = len(list_to_be_sorted)
    list_size_break_down = list_size
    sorted_list = [None]
    list_break_down = [None] * list_size_break_down
    for each_index in range(0, list_size_break_down):
        list_break_down[each_index] = [list_to_be_sorted[each_index]]


# Bilal -- initial impl of merge recursive algorithm
def divide_conquer_sort(left_list: [], right_list: []) -> []:

    sorted_left_list = [None] * len(left_list)
    sorted_right_list = [None] * len(right_list)
    if len(left_list) > 1:
        mid_section = floor(len(left_list) / 2)
        sorted_left_list = divide_conquer_sort(left_list[:mid_section], left_list[mid_section:])

    if len(right_list) > 1:
        mid_section = floor(len(right_list) / 2)
        sorted_right_list = divide_conquer_sort(right_list[:mid_section], right_list[mid_section:])

    right_index = 0
    left_index = 0
    current_index_on_result_list = 0
    result_list = [None] * (len(sorted_left_list) + len(sorted_right_list))

    while left_index < len(sorted_left_list):

        if right_index >= len(sorted_right_list):
            result_list[current_index_on_result_list] = sorted_left_list[left_index]
            left_index = left_index + 1
            current_index_on_result_list = current_index_on_result_list + 1

        while right_index < len(sorted_right_list):

            if sorted_left_list[left_index] < sorted_right_list[right_index]:
                result_list[current_index_on_result_list] = sorted_left_list[left_index]
                left_index = left_index + 1
                current_index_on_result_list = current_index_on_result_list + 1
            else:
                result_list[current_index_on_result_list] = sorted_right_list[right_index]
                right_index = right_index + 1
                current_index_on_result_list = current_index_on_result_list + 1

    return result_list


def merge_sort_b(initial_list):
    result_list = []
    if len(initial_list) > 1:
        mid_section = floor(len(initial_list) / 2)
        result_list = divide_conquer_sort(initial_list[:mid_section], initial_list[mid_section:])
    return result_list


# start of running code
if __name__ == "__main__":
    (sorted_list, random_list, reversed_list) = lists_generator(4, 4)
    #merge_sort_impl_j(reversed_list)

    print("-------------Testing Jieshu's Merge Sort Impl-------------")
    # start_time = float(time.time() * 1000)
    # result_sorted = merge_sort_impl_j(sorted_list)
    # end_time = float(time.time() * 1000)
    # print("Sorted list {} was sorted to {} in {} ms".format(sorted_list, result_sorted, (end_time - start_time)))

    start_time = float(time.time() * 1000)
    result_reversed = merge_sort_b(reversed_list)
    end_time = float(time.time() * 1000)
    print("Reversed list {} was sorted to {} in {} ms".format(reversed_list, result_reversed, (end_time - start_time)))

    # start_time = float(time.time() * 1000)
    # result_random = merge_sort_impl_j(random_list)
    # end_time = float(time.time() * 1000)
    # print("Random list {} was sorted to {} in {} ms".format(random_list, result_random, (end_time - start_time)))
    print("-------------End of Testing Jieshu's Merge Sort Impl-------------")