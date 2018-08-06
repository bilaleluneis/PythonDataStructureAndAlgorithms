from typing import Callable, Optional

__author__ = "Bilal El Uneis"
__since__ = "Aug 2018"
__email__ = "bilaleluneis@gmail.com"

"""
    Stack Data Structure Implementation using classes. this
    is a simplistic approach without diving into inheritance
    for now.. will try to apply access modifiers along the way.
"""


class Stack:
    internal_array: [int]  # array that will be used to store data for Stack instance

    def __init__(self):
        self.internal_array = [int] * 0

    def push(self, value: int):
        print("pushing {} into stack {}".format(value, self.internal_array))
        temp_array: [int] = self.increase_array_size(self.internal_array, 1)
        index: int = int(self.size(temp_array) - 1)
        temp_array[index] = value  # TODO: look into unexpected type(s) warning
        del self.internal_array
        self.internal_array = temp_array
        print("stack after push {}".format(self.internal_array))

    def pop(self) -> Optional[int]:
        index = self.size(self.internal_array) - 1
        result: int = None
        if index >= 0:
            result = self.internal_array[index]
            print("pop {} from stack {}".format(result, self.internal_array))
            temp_array = self.decrease_array_size(self.internal_array, 1)
            del self.internal_array
            self.internal_array = temp_array
            print("stack after pop {}".format(self.internal_array))
        return result

    def size(self, an_array: [int]) -> int:
        array_size: int = 0
        for _ in an_array:
            array_size = array_size + 1
        return array_size

    def increase_array_size(self, original_array: [int], by_number_of_rows: int) -> [int]:
        original_array_size = self.size(original_array)
        if by_number_of_rows < 1:
            return original_array
        elif original_array_size == 0:
            return [int] * by_number_of_rows
        else:
            new_array = [int] * (original_array_size + by_number_of_rows)
            index = 0
            while index < original_array_size:
                new_array[index] = original_array[index]
                index = index + 1
            return new_array

    def decrease_array_size(self, original_array: [int], by_number_of_rows: int) -> [int]:
        original_array_size = self.size(original_array)
        if (original_array_size - by_number_of_rows) <= 0:
            return [int] * 0
        else:
            new_array = [int] * (original_array_size - by_number_of_rows)
            index = 0
            while index < self.size(new_array):
                new_array[index] = original_array[index]
                index = index + 1
            return new_array


def main(num_push: int, num_pop: int):
    stack_instance = Stack()

    for i in range(num_push):
        stack_instance.push(i)

    print()

    for _ in range(num_pop):
        value = stack_instance.pop()
        del value  # just remove it from memory, don't really need it

    print()


# start of running code
if __name__ == "__main__":
    main(num_push=10, num_pop=17)
