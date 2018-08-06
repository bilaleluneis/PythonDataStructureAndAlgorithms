__author__ = "Jieshu Wang"
__since__ = "Aug 2018"
__email__ = "foundwonder@gmail.com"


class AbstractArray:
    _internal_array: [int]  # array that will be used to store data for Stack instance

    def __init__(self):
        self._internal_array = [int] * 0

    def _get_current_size(self):
        current_size = int(self._size(self._internal_array))
        return current_size

    def _get_value_at_index(self, index: int) ->int:
        get_value = self._internal_array[index]
        return get_value

    def _print_internal_array(self):
        print(self._internal_array)

    def _size(self, an_array: [int]) -> int:
        array_size: int = 0
        for _ in an_array:
            array_size = array_size + 1
        return array_size

    def _insert_value(self, value_to_insert: int, index_to_insert: int):
        temp_array: [int] = self._increase_array_size(1)
        original_array_size = self._get_current_size()
        if original_array_size == 0:
            temp_array = [value_to_insert]
        else:
            for x in range(index_to_insert, original_array_size-1):
                temp_array[x+1] = self._internal_array[x]
            temp_array[index_to_insert] = value_to_insert
        # del self._internal_array
        self._internal_array = temp_array

    def _increase_array_size(self, by_number_of_rows: int) -> [int]:
        original_array_size = self._size(self._internal_array)
        if by_number_of_rows < 1:
            return self._internal_array
        elif original_array_size == 0:
            return [int] * by_number_of_rows
        else:
            new_array = [int] * (original_array_size + by_number_of_rows)
            index = 0
            while index < original_array_size:
                new_array[index] = self._internal_array[index]
                index = index + 1
            return new_array

    def _decrease_array_size(self, by_number_of_rows: int) -> [int]:
        original_array_size = self._size(self._internal_array)
        if (original_array_size - by_number_of_rows) <= 0:
            return [int] * 0
        else:
            new_array = [int] * (original_array_size - by_number_of_rows)
            index = 0
            while index < self._size(new_array):
                new_array[index] = self._internal_array[index]
                index = index + 1
            return new_array


