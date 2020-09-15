from __future__ import annotations

__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Aug 2020"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

"""
Main operations of dictionaries
Dictionaries typically support so many operations −
- retrieve a __value (based on language, attempting to retrieve a missing key 
    may provide a default __value or throw an exception)
- inserting or updating a __value (typically, if the key does not exist in the dictionary, the key-__value pair is inserted; 
    if the key already exists, its corresponding __value is overwritten with the new one)
- remove or delete a key-__value pair
- test or verify for existence of a key
- iteration over the keys or values in a dictionary. 
- Note that items in a dictionary are unordered, so loops over dictionaries will return items in random order.
- keys are immutable

1. able to create an empty one
2. 
"""

from typing import TypeVar, Generic, Optional, Tuple, List, Generator
from dataclasses import dataclass
from copy import deepcopy
from immutable_types import Immutable, MyKeyType

K = TypeVar('K', int, str, tuple, Immutable)
V = TypeVar('V')


@dataclass
class KeyValuePair(Generic[K, V]):
    key: K
    value: V


KT = TypeVar('KT', int, str, tuple, Immutable)
VT = TypeVar('VT')


class Dictionary(Generic[KT, VT]):

    def __init__(self, args: Optional[List[Tuple[KT, VT]]] = None) -> None:
        self.__key_value_pairs = [KeyValuePair(key, value) for key, value in args] if args is not None else []

    def __len__(self) -> int:
        return len(self.__key_value_pairs)

    def __getitem__(self, key: KT) -> VT:
        if (key_value_pair := self.__look_up_key(key)) is not None:
            return key_value_pair.value
        raise KeyError(f'key "{key}" does not exist.')

    def __setitem__(self, key: KT, value: VT) -> None:
        if (key_value_pair := self.__look_up_key(key)) is not None:
            key_value_pair.value = value
        else:
            self.__key_value_pairs.append(KeyValuePair(key, value))

    def __contains__(self, item: KT) -> bool:
        return self.__look_up_key(item) is not None

    def items(self) -> List[Tuple[KT, VT]]:
        return [(key, self[key]) for key in self.keys()]

    def keys(self) -> List[KT]:
        return [key_value_pair.key for key_value_pair in self.__key_value_pairs]

    """Helper Methods"""

    def __look_up_key(self, key: KT) -> Optional[KeyValuePair[KT, VT]]:
        for key_value_pair in self.__key_value_pairs:
            if key_value_pair.key == key:
                return key_value_pair
        return None
