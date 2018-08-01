
__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "July 2018"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"


def insertion_sort_impl_b(list_to_sort: [int]) -> [int]:

    result_list = list(list_to_sort)
    list_size = len(list_to_sort)
    current_index = 1  # start from next element to check against previous one.
    while current_index < list_size:
        index_to_compare_from = current_index
        while index_to_compare_from > 0:
            if result_list[index_to_compare_from] < result_list[index_to_compare_from - 1]:
                swap(result_list, index_to_compare_from, (index_to_compare_from - 1))
            index_to_compare_from = index_to_compare_from - 1
        current_index = current_index + 1
    return result_list


def swap(list_to_operate_on: [int], first_index, second_index):

    first_value = list_to_operate_on[first_index]
    second_value = list_to_operate_on[second_index]
    list_to_operate_on[first_index] = second_value
    list_to_operate_on[second_index] = first_value
