__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Sep 2020"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from typing import TypeVar, Protocol, Callable
# from collections.abc import Callable
from abc import abstractmethod

T = TypeVar('T')


class MathOperation(Protocol[T]):

    __name: str

    @property
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def __call__(self, *args: T) -> T: ...


class BinaryOperation(MathOperation[T]):

    def __init__(self, op_name: str, op: Callable[[T, T], T]) -> None:
        self.__name = op_name
        self.__op = op

    @property
    def name(self) -> str:
        return self.__name

    def __call__(self, *args: T) -> T:
        if len(args) != 2:
            raise KeyError("A binary operation takes exactly two parameters.")
        return self.__op(*args)


class UnaryOperation(MathOperation[T]):

    def __init__(self, op_name: str, op: Callable[[T], T]) -> None:
        self.__name = op_name
        self.__op = op

    @property
    def name(self) -> str:
        return self.__name

    def __call__(self, *args: T) -> T:
        if len(args) != 1:
            raise KeyError("A unary operation takes exactly one parameter.")
        return self.__op(*args)




