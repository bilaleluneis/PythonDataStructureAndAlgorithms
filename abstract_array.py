__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2018"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from typing import Optional, Type, SupportsInt, List

"""
    This will eventually become a True Abstract class. for now
    we have everything at private or protected scope, so creating
    instance of this class is useless on its own.
"""


class AbstractArray:

    def __init__(self):
        """
        __internal_array is a list of type int or anything that supports type int
        needed to add SupportsInt to clear warnings from PyCharm about
        int() call that threw back that it expected type of SupportsInt and not
        Type[int]
        """
        self.__internal_array: List[Type[int, SupportsInt]] = [int] * 0

    # returns a string representation of AbstractArray internal information
    def __str__(self):
        discription: str = "["

        for entry in self.__internal_array:
            discription += "{}, ".format(entry)

        discription = discription[:-2]  # remove last space and last ','
        discription += "]"
        return discription

    @property
    def _size(self) -> int:
        array_size: int = 0
        for _ in self.__internal_array:
            array_size += 1
        return array_size

    def _get_value_at_index(self, index: int) -> Optional[int]:
        if index < 0 or index >= self._size:
            return None  # index provided falls out of range of the array!
        else:
            get_value: Type[int, SupportsInt] = self.__internal_array[index]
            return int(get_value)  # return a copy of that value and not reference!

    def _assign_value_to_index(self, value_to_insert: int, at_index: int):
        if at_index < 0 or at_index >= self._size:
            return
        else:
            self.__internal_array[at_index] = value_to_insert

    def _increase_array_size(self, by_number_of_rows: int):
        original_array_size = self._size
        if by_number_of_rows < 1:
            return  # nothing to resize , just return
        elif original_array_size == 0:
            self.__internal_array = [int] * by_number_of_rows
        else:
            new_array = [int] * (original_array_size + by_number_of_rows)
            index = 0
            while index < original_array_size:
                new_array[index] = self.__internal_array[index]
                index += 1
            del self.__internal_array
            self.__internal_array = new_array

    def _decrease_array_size(self, by_number_of_rows: int):
        original_array_size = self._size
        if (original_array_size - by_number_of_rows) <= 0:
            del self.__internal_array
            self.__internal_array = [int] * 0
        else:
            new_array = [int] * (original_array_size - by_number_of_rows)
            index = 0
            while index < self._size:
                new_array[index] = self.__internal_array[index]
                index += 1
            del self.__internal_array
            self.__internal_array = new_array
