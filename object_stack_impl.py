from typing import Optional
from abstract_array import AbstractArray

__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "Aug 2018"
__email__ = "bilaleluneis@gmail.com"

"""
    Stack Data Structure Implementation using classes. this
    this is now updated to use inheritance and access modifiers.
"""


class Stack(AbstractArray):

    def __init__(self, object_type: str = "Stack"):
        super().__init__()
        print("new instance of{} created! {}".format(object_type, self))

    def push(self, value: int):
        self._increase_array_size(by_number_of_rows=1)
        self._assign_value_to_index(value, self._size - 1)

    def pop(self) -> Optional[int]:
        current_size = self._size
        if current_size > 0:
            value_popped = self._get_value_at_index(self._size - 1)
            self._decrease_array_size(by_number_of_rows=1)
            return value_popped


def main(num_push: int, num_pop: int):
    stack_instance = Stack()

    for i in range(num_push):
        print("pushing {} into {} {}".format(i, "stack", stack_instance))
        stack_instance.push(i)
        print("{} after push {}".format("stack", stack_instance))

    print()

    for _ in range(num_pop):
        value = stack_instance.pop()
        print("{} after {} is poped {}".format("stack", value, stack_instance))
        del value  # just remove it from memory, don't really need it

    print()


# start of running code
if __name__ == "__main__":
    main(num_pop=17, num_push=10)
