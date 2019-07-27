__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2018"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from typing import Optional, Type, SupportsInt, List
from abc import ABC, abstractmethod


class ArrayIndexOutOfBoundError(Exception):
    pass


class AbstractArray(ABC):

    def __init__(self):
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
    def set(self, value: int, at_index: int):
        pass

    @abstractmethod
    def insert(self, value: int, at_index: Optional[int] = None):
        pass


class ArrayListImpl(AbstractArray):

    def __init__(self):
        super().__init__()
        self.__internal_array: List[Type[int, SupportsInt]] = [int] * 0
        self._class_name: str = type(self).__name__

    def __str__(self):
        description: str = "{} [".format(self._class_name)

        for entry in self.__internal_array:
            description += "{}, ".format(entry)

        description = description[:-2]  # remove last space and last ','
        description += "]"
        return description

    @property
    @abstractmethod
    def size(self) -> int:
        array_size: int = 0
        for _ in self.__internal_array:
            array_size += 1
        return array_size

    @abstractmethod
    def get(self, at_index: int) -> Optional[int]:  # returns an int or None
        if at_index < 0 or at_index >= self.size:
            return None  # index provided falls out of range of the array!
        else:
            get_value: Type[int, SupportsInt] = self.__internal_array[at_index]
            return int(get_value)  # return a copy of that value and not reference!

    @abstractmethod
    def remove(self, at_index: Optional[int] = None) -> Optional[int]:
        resolved_index: int

        if at_index is None:
            resolved_index = self.size - 1
        else:
            resolved_index = at_index

        value_at_index: Optional[int] = self.get(resolved_index)

        if value_at_index is not None:
            new_array: List[Type[int, SupportsInt]] = [int] * (self.size - 1)

            for index in range(self.size):
                if index != resolved_index:
                    new_array += int(self.__internal_array[index])

            del self.__internal_array
            self.__internal_array = new_array

        return value_at_index

    @abstractmethod
    def set(self, value: int, at_index: int):
        if at_index < 0 or at_index >= self.size:
            class_name: str = type(self).__name__
            error: str = "{} _set[{}] = {} Failed, index {} is invalid!".format(class_name, at_index, value, at_index)
            raise ArrayIndexOutOfBoundError(error)
        else:
            self.__internal_array[at_index] = int(value)  # make a copy and place in index of the array

    @abstractmethod
    def insert(self, value: int, at_index: Optional[int] = None):
        inserted_value: List[Type[int, SupportsInt]] = [int] * 1
        inserted_value[0] = int(value)
        if at_index is None:
            self.__internal_array += inserted_value
        elif at_index in range(0, self.size - 1):
            left_array: List[Type[int, SupportsInt]] = list(self.__internal_array[:at_index])
            right_array: List[Type[int, SupportsInt]] = list(self.__internal_array[at_index:])
            del self.__internal_array
            self.__internal_array = left_array + inserted_value + right_array
        else:
            class_name: str = type(self).__name__
            error: str = "{}._insert[{}]={} Failed, index {} is invalid!".format(class_name, at_index, value, at_index)
            raise ArrayIndexOutOfBoundError(error)


class ArrayNodeImpl(AbstractArray):

    def __init__(self):
        super().__init__()
        self.__size: int = 0

    @property
    def size(self) -> int:
        return self.__size

    def get(self, at_index: int) -> Optional[int]:
        pass

    def remove(self, at_index: Optional[int] = None) -> Optional[int]:
        pass

    def set(self, value: int, at_index: int):
        pass

    def insert(self, value: int, at_index: Optional[int] = None):
        pass
