from typing import Optional

__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "Aug 2018"
__email__ = "bilaleluneis@gmail.com"

"""
    Stack Data Structure Implementation using classes. this
    is a simplistic approach without diving into inheritance
    for now.. will try to apply access modifiers along the way.
"""


class Stack:
    __internal_array: [int]  # array that will be used to store data for Stack instance

    def __init__(self):
        self.__internal_array = [int] * 0
        print("new instance of Stack created!")

    def push(self, value: int):
        print("pushing {} into stack {}".format(value, self.__internal_array))
        temp_array: [int] = self.__increase_array_size(1)
        index: int = int(self.__size(temp_array) - 1)
        temp_array[index] = value  # TODO: look into unexpected type(s) warning
        del self.__internal_array
        self.__internal_array = temp_array
        print("stack after push {}".format(self.__internal_array))

    def pop(self) -> Optional[int]:
        index = self.__size(self.__internal_array) - 1
        result: int = None
        if index >= 0:
            result = self.__internal_array[index]
            print("pop {} from stack {}".format(result, self.__internal_array))
            temp_array = self.__decrease_array_size(1)
            del self.__internal_array
            self.__internal_array = temp_array
            print("stack after pop {}".format(self.__internal_array))
        return result

    def __size(self, an_array: [int]) -> int:
        array_size: int = 0
        for _ in an_array:
            array_size = array_size + 1
        return array_size

# put double underscores in front of the names
# of the method functions to make them private,
# so they are invisible from the outside.
    def __increase_array_size(self, by_number_of_rows: int) -> [int]:
        original_array_size = self.__size(self.__internal_array)
        if by_number_of_rows < 1:
            return self.__internal_array
        elif original_array_size == 0:
            return [int] * by_number_of_rows
        else:
            new_array = [int] * (original_array_size + by_number_of_rows)
            index = 0
            while index < original_array_size:
                new_array[index] = self.__internal_array[index]
                index = index + 1
            return new_array

    def __decrease_array_size(self, by_number_of_rows: int) -> [int]:
        original_array_size = self.__size(self.__internal_array)
        if (original_array_size - by_number_of_rows) <= 0:
            return [int] * 0
        else:
            new_array = [int] * (original_array_size - by_number_of_rows)
            index = 0
            while index < self.__size(new_array):
                new_array[index] = self.__internal_array[index]
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
    main(num_pop=17, num_push=10)
