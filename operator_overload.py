from __future__ import annotations

__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Sep 2020"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from typing import cast


class MyInteger:

    def __init__(self, value: int) -> None:
        self.__value: int = value

    @property
    def value(self) -> int:
        return self.__value

    def __lt__(self, other: MyInteger) -> bool:
        return self.value < other.value

    def __eq__(self, other: object) -> bool:
        cast_other = cast(MyInteger, other)
        return not (self < cast_other or cast_other < self)

    def __ne__(self, other: object) -> bool:
        cast_other = cast(MyInteger, other)
        return not self == cast_other

    def __gt__(self, other: MyInteger) -> bool:
        return not (self < other or self == other)
