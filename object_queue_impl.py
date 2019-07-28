__author__ = "Jieshu Wang & Bilal El Uneis"
__since__ = "Aug 2018"
__email__ = "foundwonder@gmail.com"

from abstract_array import *


class QueueListImplInheritance(ArrayListImpl):

    def __init__(self):
        super().__init__()

    def enqueue(self, value) -> None:
        self.insert(value)

    def dequeue(self) -> Optional[int]:
        return self.remove(0)


class QueueListImplComposition(object):

    def __init__(self):
        self.__internal_queue: ArrayListImpl = ArrayListImpl()

    @property
    def size(self):
        return self.__internal_queue.size

    def __str__(self) -> str:
        description = str(self.__internal_queue)
        description = description.replace("ArrayListImpl", type(self).__name__)
        return description

    def enqueue(self, value) -> None:
        self.__internal_queue.insert(value)

    def dequeue(self) -> Optional[int]:
        return self.__internal_queue.remove(0)
