__author__ = "Jieshu Wang"
__since__ = "July 2018"
__email__ = "foundwonder@gmail.com"

from numpy import random as random_generator
from numpy import ceil as round_up
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


# start of running code
if __name__ == "__main__":
    (sorted_list, random_list, reversed_list) = lists_generator(10, 10)
    #merge_sort_impl_j(reversed_list)

    print("-------------Testing Jieshu's Merge Sort Impl-------------")
    start_time = timer.now()
    result_sorted = merge_sort_impl_j(sorted_list)
    end_time = timer.now()
    print("Sorted list {} was sorted to {} in {} ms".format(sorted_list, result_sorted, (end_time - start_time)))

    start_time = timer.now()
    result_reversed = merge_sort_impl_j(reversed_list)
    end_time = timer.now()
    print("Reversed list {} was sorted to {} in {} ms".format(reversed_list, result_reversed, (end_time - start_time)))

    start_time = timer.now()
    result_random = merge_sort_impl_j(random_list)
    end_time = timer.now()
    print("Random list {} was sorted to {} in {} ms".format(random_list, result_random, (end_time - start_time)))
    print("-------------End of Testing Jieshu's Merge Sort Impl-------------")