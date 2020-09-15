from __future__ import annotations

__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Aug 2020"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from typing import TypeVar, Generic, List
from abc import ABC
from copy import deepcopy

T = TypeVar('VectorElementType')


class Immutable(ABC, Generic[T]):

    def __init__(self, value: T) -> None:
        self.__value: T = value

    @property
    def key(self) -> T:
        return deepcopy(self.__value)


class MyKeyType(Immutable):
    def __init__(self, value: List[str]) -> None:
        super().__init__(value)
