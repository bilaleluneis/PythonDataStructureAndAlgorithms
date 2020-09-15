from __future__ import annotations
__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Sep 2020"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from typing import TypeVar, Protocol
from abc import abstractmethod

T = TypeVar('T')


class Number(Protocol[T]):

    __value: T

    @property
    @abstractmethod
    def value(self) -> T: ...

    @abstractmethod
    def __add__(self, other: Number[T]) -> Number[T]: ...


class Integer(Number[int]):

    def __init__(self, value: int):
        self.__value: int = value

    @property
    def value(self) -> int:
        return self.__value

    def __add__(self, other: Number[int]) -> Integer:
        return Integer(self.value + other.value)


class Float(Number[float]):

    def __init__(self, value: float):
        self.__value: float = value

    @property
    def value(self) -> float:
        return self.__value

    def __add__(self, other: Number[float]) -> Float:
        return Float(self.value + other.value)

