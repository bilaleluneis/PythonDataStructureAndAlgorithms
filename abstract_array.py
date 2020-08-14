__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2018"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from typing import Type, List
from abc import ABC, abstractmethod
from node import *


class ArrayIndexOutOfBoundError(Exception):
    pass


class AbstractArray(ABC):

    def __init__(self) -> None:
        self._class_name: str = type(self).__name__

    @property
    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def get(self, at_index: int) -> Optional[int]:  # returns an int or None
        pass

    @abstractmethod
    def remove(self, at_index: Optional[int] = None) -> Optional[int]:
        pass

    @abstractmethod
    def set(self, value: int, at_index: int) -> None:
        pass

    @abstractmethod
    def insert(self, value: int, at_index: Optional[int] = None) -> None:
        pass


class ArrayListImpl(AbstractArray):

    def __init__(self) -> None:
        super().__init__()
        self.__internal_array: List[Type[int, SupportsInt]] = [int] * 0

    def __str__(self) -> str:
        description: str = "{} [".format(self._class_name)

        for entry in self.__internal_array:
            description += "{}, ".format(entry)

        if self.size > 0:
            description = description[:-2]  # remove last space and last ','

        description += "]"
        return description

    @property
    def size(self) -> int:
        array_size: int = 0
        for _ in self.__internal_array:
            array_size += 1
        return array_size

    def get(self, at_index: int) -> Optional[int]:  # returns an int or None
        if at_index < 0 or at_index >= self.size:
            return None  # index provided falls out of range of the array!
        else:
            get_value: Type[int, SupportsInt] = self.__internal_array[at_index]
            return int(get_value)  # return a copy of that value and not reference!

    def remove(self, at_index: Optional[int] = None) -> Optional[int]:
        resolved_index: int

        if at_index is None:
            resolved_index = self.size - 1
        else:
            resolved_index = at_index

        value_at_index: Optional[int] = self.get(resolved_index)

        if value_at_index is not None:
            new_array: List[Type[int, SupportsInt]] = [int] * (self.size - 1)
            new_array_index: int = 0

            for index in range(self.size):
                if index != resolved_index:
                    new_array[new_array_index] = (int(self.__internal_array[index]))
                    new_array_index += 1

            del self.__internal_array
            self.__internal_array = new_array

        return value_at_index

    def set(self, value: int, at_index: int) -> None:
        if at_index < 0 or at_index >= self.size:
            class_name: str = self._class_name
            error: str = "{} _set[{}] = {} Failed, index {} is invalid!".format(class_name, at_index, value, at_index)
            raise ArrayIndexOutOfBoundError(error)
        else:
            self.__internal_array[at_index] = int(value)  # make a copy and place in index of the array

    def insert(self, value: int, at_index: Optional[int] = None) -> None:
        inserted_value: List[Type[int, SupportsInt]] = [int] * 1
        inserted_value[0] = int(value)
        if at_index is None:
            self.__internal_array += inserted_value
        elif at_index in range(0, self.size):
            left_array: List[Type[int, SupportsInt]] = list(self.__internal_array[:at_index])
            right_array: List[Type[int, SupportsInt]] = list(self.__internal_array[at_index:])
            del self.__internal_array
            self.__internal_array = left_array + inserted_value + right_array
        else:
            class_name: str = self._class_name
            error: str = "{}._insert[{}]={} Failed, index {} is invalid!".format(class_name, at_index, value, at_index)
            raise ArrayIndexOutOfBoundError(error)


class ArrayNodeImpl(AbstractArray):

    def __init__(self) -> None:
        super().__init__()
        self.__node: Optional[Node] = None

    def __str__(self) -> str:
        description: str = "{} [".format(self._class_name)

        if self.size > 0:
            for i in range(self.size):
                current_value = self.get(i)
                description += "{}, ".format(current_value)

            description = description[:-2]
        description += "]"

        return description

    @property
    def size(self) -> int:
        return self.__offspring_counter(self.__node)

    def get(self, at_index: int) -> Optional[int]:
        if at_index < 0 or at_index >= self.size:
            return None
        else:
            return self.__get_node(at_index).value

    def remove(self, at_index: Optional[int] = None) -> Optional[int]:
        resolved_index: Optional[int] = at_index

        if at_index is None:
            resolved_index = self.size - 1

        value_at_index: Optional[int] = self.get(resolved_index)

        if value_at_index is not None:  # if the node does exist
            node_to_remove = self.__get_node(resolved_index)
            last_node = self.__find_last_node()
            second_to_last_node = self.__get_parent_node(last_node.id)
            node_to_remove.id = last_node.id
            node_to_remove.value = last_node.value
            if second_to_last_node is None:  # if there's only one node
                self.__node = None
            else:
                second_to_last_node.child = None
                self.__shift_id(resolved_index+1, -1)

        return value_at_index

    def set(self, value: int, at_index: int) -> None:
        node_to_set = self.__get_node(at_index)
        if node_to_set is not None:
            node_to_set.value = value

    def insert(self, value: int, at_index: Optional[int] = None) -> None:
        resolved_index: Optional[int] = at_index

        if at_index is None:
            resolved_index: int = int(self.size)

        if resolved_index in range(self.size+1):  # if index = size, put it at the end.
            self.__shift_id(resolved_index, 1)
            last_node: Node = self.__find_last_node()
            if last_node is None:  # if the array is empty
                self.__node: Node = Node(resolved_index, value)  # resolved_index can only be 0 if array is empty
            else:
                last_node.child = Node(resolved_index, value)
        else:
            class_name: str = self._class_name
            error: str = "{}._insert[{}]={} Failed, index {} is invalid!".format(class_name, at_index, value, at_index)
            raise ArrayIndexOutOfBoundError(error)

    """ utility methods """

    def __get_node(self, at_index: int) -> Optional[Node]:
        root_node = self.__node
        while root_node is not None:
            if root_node.id == at_index:
                return root_node
            else:
                root_node = root_node.child
        return root_node

    def __get_parent_node(self, at_index: int) -> Optional[Node]:
        root_node: Node = self.__node
        if root_node.id == at_index:
            return None
        else:
            while root_node is not None and root_node.child is not None:
                if root_node.child.id == at_index:
                    return root_node
                else:
                    root_node = root_node.child

    # def __get_parent_node_2(self):

    def __offspring_counter(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        else:
            return self.__offspring_counter(node.child) + 1

    def __shift_id(self, from_index: int, number: int) -> None:
        root_node = self.__node
        while root_node is not None:
            if root_node.id >= from_index:
                root_node.id += number
            root_node = root_node.child

    def __find_last_node(self) -> Optional[Node]:
        root_node: Optional[Node] = self.__node
        if root_node is None:
            return None
        else:
            while root_node.child is not None:
                root_node = root_node.child
            return root_node

