
__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "July 2018"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from test_data_generator import *


def insertion_sort_impl_b(list_to_sort: [int], visualize: bool = False) -> [int]:
    result_list = list(list_to_sort)
    list_size = len(list_to_sort)
    current_index = 1  # start from next element to check against previous one.
    if visualize:
        print("Before Sort: {}".format(result_list))
    while current_index < list_size:
        index_to_compare_from = current_index
        while index_to_compare_from > 0:
            if result_list[index_to_compare_from] < result_list[index_to_compare_from - 1]:
                swap(result_list, index_to_compare_from, (index_to_compare_from - 1))
                if visualize:
                    print(result_list)
            index_to_compare_from = index_to_compare_from - 1
        current_index = current_index + 1
    if visualize:
        print("After Sort: {}".format(result_list))
    return result_list


def swap(list_to_operate_on: [int], first_index, second_index):

    first_value = list_to_operate_on[first_index]
    second_value = list_to_operate_on[second_index]
    list_to_operate_on[first_index] = second_value
    list_to_operate_on[second_index] = first_value


def insertion_sort_impl_j(list_to_be_sorted: [], visualize: bool = False) ->[]:
    result_list = [list_to_be_sorted[0]]
    if visualize:
        print("Before Sort: {}".format(list_to_be_sorted))
        print(result_list)
    for element in list_to_be_sorted[1:]:
        if element > result_list[-1]:
            result_list.append(element)
        elif element < result_list[0]:
            result_list.insert(0, element)
        else:
            for x in list(range(len(result_list) - 1)):
                if result_list[x] <= element <= result_list[x+1]:
                    result_list.insert(x+1, element)
                    break
        if visualize:
            print(result_list)
    if visualize:
        print("After Sort: {}".format(result_list))
    return result_list


# start of running code
if __name__ == "__main__":
    (sorted_list, random_list, reversed_list) = lists_generator(10, 10)
    visualization_on: bool = False
    # analyze("Bilal's Insertion Sort", insertion_sort_impl_b, random_list, visualization_on)
    analyze("Jieshu's Insertion Sort", insertion_sort_impl_j, [8, 8, 7, 4, 2, 2, 3, 0, 6, 3], visualization_on)
