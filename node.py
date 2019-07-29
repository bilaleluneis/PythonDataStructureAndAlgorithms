from __future__ import annotations

__author__ = "Bilal El Uneis"
__since__ = "July 2019"
__email__ = "bilaleluneis@gmail.com"

from typing import TypeVar, SupportsInt, Optional

# Type is of or subtype of int, bool
T = TypeVar("T", int, bool, SupportsInt)


class NodeAlreadyInitializedError(Exception):
    pass


class InvalidTypeError(Exception):
    pass


class Node:
    def __init__(self, uid: int, value: T) -> None:
        self.__uid = uid
        self.__value = value
        self.__child_node: Optional[Node] = None

    @property
    def value(self) -> T:
        if type(self.__value) is int:
            return int(self.__value)
        else:  # must be a boolean type
            return bool(self.__value)

    @value.setter
    def value(self, new_value: T):
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
    def id(self, new_id: int):
        if type(new_id) is int:
            self.__uid = int(new_id)
        else:
            raise InvalidTypeError("The type of input value is invalid.")

    @property
    def child(self) -> Node:
        return self.__child_node

    def init_child(self, uid: int, value: T) -> None:
        if self.child is None:
            self.__child_node = Node(uid, value)
        else:
            error: str = "Child of Node with id ={} already initalized with id={} and value={}".format(self.id,
                                                                                                       self.child.id,
                                                                                                       self.child.value)
            raise NodeAlreadyInitializedError(error)
