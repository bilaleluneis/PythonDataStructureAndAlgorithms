
__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "July 2018"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from numpy import random as random_generator
import time


# Generate several lists to be sorted and return a tuple
# data structure that will contain the following:
# an already sorted list, a sorted list in reverse and
# a randomly unsorted list of numbers. this will be used
# to test sorting algorithms for best, common and worst case
# scenarios !
def lists_generator(end_number: int, list_size: int) -> ([int], [int], [int]):
    already_sorted_list = list(range(list_size))
    random_sorted_list = random_generator.randint(end_number, size=list_size).tolist()
    reverse_sorted_list = already_sorted_list[::-1]
    return already_sorted_list, random_sorted_list, reverse_sorted_list


# takes a function that accepts array/list of integers.
# returns array/list of integers and a float representing
# the execution time of the function in milliseconds.
def time_it(function_to_time: callable([int]), function_input: [int]) -> ([int], float):
    start_time = float(time.time() * 1000)
    function_output = function_to_time(function_input)
    end_time = float(time.time() * 1000)
    return function_output, (end_time - start_time)

