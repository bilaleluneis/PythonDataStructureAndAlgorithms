from typing import Optional
from abstract_array import AbstractArray

__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "Aug 2018"
__email__ = "bilaleluneis@gmail.com"

"""
    Stack Data Structure Implementation using classes. this
    is a simplistic approach without diving into inheritance
    for now.. will try to apply access modifiers along the way.
"""


class Stack(AbstractArray):

    def __init__(self):
        super().__init__()
        print("new instance of Stack created!")

    def push(self, value: int):
        print("pushing {} into stack".format(value), self._print_internal_array())
        array_size = self._get_current_size()
        self._insert_value(value, array_size - 1)
        # temp_array: [int] = self._increase_array_size(1)
        # index: int = int(self._size(temp_array) - 1)
        # temp_array[index] = value  # TODO: look into unexpected type(s) warning
        # del self._internal_array
        # self._internal_array = temp_array
        # print("stack after push {}".format(self._internal_array))

    def pop(self) -> Optional[int]:
        array_size = self._get_current_size()
        index = array_size - 1
        result: int = None
        if index >= 0:
            result = self._get_value_at_index(index)
            self._decrease_array_size(1)
        return result
        # index = self._size(self._internal_array) - 1
        # result: int = None
        # if index >= 0:
        #     result = self._internal_array[index]
        #     print("pop {} from stack {}".format(result, self._internal_array))
        #     temp_array = self._decrease_array_size(1)
        #     del self._internal_array
        #     self._internal_array = temp_array
        #     print("stack after pop {}".format(self._internal_array))
        # return result


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
