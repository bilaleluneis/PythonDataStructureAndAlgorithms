__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Sep 2020"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from typing import TypeVar, Sequence, Optional, Collection, Generator, List, Sized
from vector import CPUVector, VectorElementType

T = TypeVar('T')


def linear_search(search_array: Sequence[T], target: T) -> Optional[int]:
    for index in range(len(search_array)):
        if search_array[index] == target:
            return index
    return None



