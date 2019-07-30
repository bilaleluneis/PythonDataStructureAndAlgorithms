from __future__ import annotations

__author__ = "Bilal El Uneis"
__since__ = "July 2019"
__email__ = "bilaleluneis@gmail.com"

from typing import TypeVar, SupportsInt, Optional

# Type is of or subtype of int, bool
T = TypeVar("T", int, bool, SupportsInt)


class InvalidTypeError(Exception):
    pass


class Node:
    def __init__(self, uid: int, a_value: T) -> None:
        self.__uid: Optional[int] = None
        self.__value: Optional[T] = None
        self.__child_node: Optional[Node] = None
        self.value = a_value
        self.id = uid

    def __repr__(self) -> str:
        return "Node(id={}, value={})".format(self.id, self.value)

    @property
    def value(self) -> T:
        if type(self.__value) is int:
            return int(self.__value)
        else:  # must be a boolean type
            return bool(self.__value)

    @value.setter
    def value(self, new_value: T) -> None:
        if type(new_value) is int:
            self.__value = int(new_value)
        elif type(new_value) is bool:
            self.__value = bool(new_value)
        else:
            raise InvalidTypeError("The type of input value is invalid.")

    @property
    def id(self) -> int:
        return int(self.__uid)

    @id.setter
    def id(self, new_id: int) -> None:
        if type(new_id) is int:
            self.__uid = int(new_id)
        else:
            raise InvalidTypeError("The type of input value is invalid.")

    @property
    def child(self) -> Optional[Node]:
        return self.__child_node

    @child.setter
    def child(self, node: Optional[Node]) -> None:
        if node is None:
            self.__child_node = None
        else:
            self.__child_node = Node(node.id, node.value)
