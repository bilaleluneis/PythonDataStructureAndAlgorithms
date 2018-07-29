
__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "July 2018"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from numpy import random as random_generator
from datetime import datetime as timer


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


# Check if a list is sorted correctly
def sorting_finished_check(list_to_check):
    index = 0
    check = True
    while index < len(list_to_check) - 1:
        if list_to_check[index] > list_to_check[index + 1] or not check:
            check = False
        index = index + 1
    return check


"""
  Author: Bilal El Uneis
  bubble_sort_impl_b:
  another implementation of bubble sort
  algorithm
"""


def bubble_sort_impl_b(list_to_be_sorted):

    list_size = len(list_to_be_sorted)
    current_index = list_size - 1
    sorted_array = list(list_to_be_sorted)
    number_of_iterations = 0

    while number_of_iterations < (list_size - 1):

        while current_index > 0:  # 0 is first index in array
            current_element = sorted_array[current_index]
            previous_element = sorted_array[current_index - 1]
            if current_element < previous_element:
                sorted_array[current_index] = previous_element
                sorted_array[current_index - 1] = current_element
            current_index = current_index - 1

        number_of_iterations = number_of_iterations + 1
        current_index = list_size - 1

    return sorted_array


# Jieshu's bubble sort impl
def bubble_sort_impl_j(list_to_be_sorted):

    result_list = list(list_to_be_sorted)
    sorting_finished = sorting_finished_check(result_list)
    while not sorting_finished:
        index = 0
        while index < len(result_list) - 1:
            if result_list[index] > result_list[index + 1]:
                sort_num = result_list[index]
                result_list.pop(index)
                result_list.insert(index + 1, sort_num)
            index = index + 1
        sorting_finished = sorting_finished_check(result_list)
    return result_list


# start of running code
if __name__ == "__main__":
    (sorted_list, random_list, reversed_list) = lists_generator(100, 30)

    print("-------------Testing Bilal's Bubble Sort Impl-------------")
    start_time = timer.now()
    result_sorted = bubble_sort_impl_b(sorted_list)
    end_time = timer.now()
    print("list {} was sorted to {} in {} ms".format(sorted_list, result_sorted, (end_time - start_time)))

    start_time = timer.now()
    result_reversed = bubble_sort_impl_b(reversed_list)
    end_time = timer.now()
    print("list {} was sorted to {} in {} ms".format(reversed_list, result_reversed, (end_time - start_time)))

    start_time = timer.now()
    result_random = bubble_sort_impl_b(random_list)
    end_time = timer.now()
    print("list {} was sorted to {} in {} ms".format(random_list, result_random, (end_time - start_time)))
    print("-------------End of Testing Bilal's Bubble Sort Impl-------------")

    print()  # creating a new line

    print("-------------Testing Jieshu's Bubble Sort Impl-------------")
    start_time = timer.now()
    result_sorted = bubble_sort_impl_j(sorted_list)
    end_time = timer.now()
    print("list {} was sorted to {} in {} ms".format(sorted_list, result_sorted, (end_time - start_time)))

    start_time = timer.now()
    result_reversed = bubble_sort_impl_j(reversed_list)
    end_time = timer.now()
    print("list {} was sorted to {} in {} ms".format(reversed_list, result_reversed, (end_time - start_time)))

    start_time = timer.now()
    result_random = bubble_sort_impl_j(random_list)
    end_time = timer.now()
    print("list {} was sorted to {} in {} ms".format(random_list, result_random, (end_time - start_time)))
    print("-------------End of Testing Jieshu's Bubble Sort Impl-------------")
