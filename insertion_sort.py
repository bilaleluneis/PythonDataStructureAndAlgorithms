
__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "July 2018"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from test_data_generator import *


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


def insertion_sort_impl_j(list_to_be_sorted: []) ->[]:
    sorted_list = [list_to_be_sorted[0]]
    for element in list_to_be_sorted[1:]:
        if element > sorted_list[-1]:
            sorted_list.append(element)
        elif element < sorted_list[0]:
            sorted_list.insert(0, element)
        else:
            for x in list(range(len(sorted_list) - 1)):
                if sorted_list[x] <= element <= sorted_list[x+1]:
                    sorted_list.insert(x+1, element)
                    break
    return sorted_list


# start of running code
if __name__ == "__main__":
    (sorted_list, random_list, reversed_list) = lists_generator(10, 10)

    print("-------------Testing Bilal's Insertion Sort Impl-------------")
    (result, time_ms) = time_it(insertion_sort_impl_b, sorted_list)
    print("In {} ms, list {} was sorted to {}".format(time_ms, sorted_list, result))
    # print(compare(sorted(sorted_list), result))

    (result, time_ms) = time_it(insertion_sort_impl_b, random_list)
    print("In {} ms, list {} was sorted to {}".format(time_ms, random_list, result))
   # print(compare(sorted(random_list), result))

    (result, time_ms) = time_it(insertion_sort_impl_b, reversed_list)
    print("In {} ms, list {} was sorted to {}".format(time_ms, reversed_list, result))
    #print(compare(sorted(reversed_list), result))
    print("-------------End of Testing Bilal's Insertion Sort Impl-------------")

    print()  # creating a new line

    print("-------------Testing Jieshu's Insertion Sort Impl-------------")
    (result, time_ms) = time_it(insertion_sort_impl_j, sorted_list)
    #print(compare(sorted(sorted_list), result))
    print("In {} ms, list {} was sorted to {}".format(time_ms, sorted_list, result))

    (result, time_ms) = time_it(insertion_sort_impl_j, random_list)
   # print(compare(sorted(random_list), result))
    print("In {} ms, list {} was sorted to {}".format(time_ms, random_list, result))

    (result, time_ms) = time_it(insertion_sort_impl_j, reversed_list)
   # print(compare(sorted(reversed_list), result))
    print("In {} ms, list {} was sorted to {}".format(time_ms, reversed_list, result))
    print("-------------End of Jieshu's Insertion Sort Impl-------------")