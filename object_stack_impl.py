__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "Aug 2018"
__email__ = "bilaleluneis@gmail.com, foundwonder@gmail.com"

"""
    Stack Data Structure Implementation using classes. this
    this is now updated to use inheritance and access modifiers.
"""

from abstract_array import *


class StackListImpl(ArrayListImpl):

    def __init__(self):
        super().__init__()

    def push(self, value) -> None:
        self.insert(value)

    def pop(self) -> Optional[int]:
        return self.remove()


class StackListCompoImpl(object):

    def __init__(self):
        self.__internal_stack: ArrayListImpl = ArrayListImpl()

    @property
    def size(self):
        return self.__internal_stack.size

    def __str__(self) -> str:
        description = str(self.__internal_stack)
        description = description.replace("ArrayListImpl", type(self).__name__)
        return description

    def push(self, value) -> None:
        self.__internal_stack.insert(value)

    def pop(self) -> Optional[int]:
        return self.__internal_stack.remove()
