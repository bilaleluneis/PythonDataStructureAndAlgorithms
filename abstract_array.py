__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2018"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from typing import Optional


"""
    This will eventually become a True Abstract class. for now
    we have everything at private or protected scope, so creating
    instance of this class is useless on its own.
"""


class AbstractArray:

    __internal_array: [int]  # array that will be used to store data for Stack instance

    def __init__(self):
        self.__internal_array = [int] * 0

    # returns a string representation of AbstractArray internal information
    def __str__(self):
        return "{}".format(self.__internal_array)

    def _get_current_size(self) -> int:
        current_size = int(self.__size(self.__internal_array))
        return current_size

    def _get_value_at_index(self, index: int) -> Optional[int]:
        if index < 0 or index >= self._get_current_size():
            return None  # index provided falls out of range of the array!
        else:
            get_value = int(self.__internal_array[index])  # return a copy of that value and not reference!
            return get_value

    @staticmethod
    def __size(an_array: [int]) -> int:
        array_size: int = 0
        for _ in an_array:
            array_size = array_size + 1
        return array_size

    def _assign_value_to_index(self, value_to_insert: int, at_index: int):
        if at_index < 0 or at_index >= self._get_current_size():
            return
        else:
            self.__internal_array[at_index] = value_to_insert

    def _increase_array_size(self, by_number_of_rows: int):
        original_array_size = self.__size(self.__internal_array)
        if by_number_of_rows < 1:
            return  # nothing to resize , just return
        elif original_array_size == 0:
            self.__internal_array = [int] * by_number_of_rows
        else:
            new_array = [int] * (original_array_size + by_number_of_rows)
            index = 0
            while index < original_array_size:
                new_array[index] = self.__internal_array[index]
                index = index + 1
            del self.__internal_array
            self.__internal_array = new_array

    def _decrease_array_size(self, by_number_of_rows: int):
        original_array_size = self.__size(self.__internal_array)
        if (original_array_size - by_number_of_rows) <= 0:
            del self.__internal_array
            self.__internal_array = [int] * 0
        else:
            new_array = [int] * (original_array_size - by_number_of_rows)
            index = 0
            while index < self.__size(new_array):
                new_array[index] = self.__internal_array[index]
                index = index + 1
            del self.__internal_array
            self.__internal_array = new_array
