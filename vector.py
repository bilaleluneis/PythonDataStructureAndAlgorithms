from __future__ import annotations

__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Sep 2020"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from typing import TypeVar, Optional, Protocol, runtime_checkable, Collection, Type
from abc import abstractmethod

VectorElementType = TypeVar('VectorElementType', int, float)


@runtime_checkable
class VectorInterface(Protocol[VectorElementType]):
    __value: Collection[VectorElementType]

    @abstractmethod
    def __len__(self) -> int: ...

    @abstractmethod
    def __add__(self, other: VectorInterface[VectorElementType]) -> VectorInterface[VectorElementType]: ...

    @property
    @abstractmethod
    def value(self) -> Collection[VectorElementType]: ...


class CPUVector(VectorInterface[VectorElementType]):
    def __init__(self, value: Optional[Collection[VectorElementType]] = None) -> None:
        self.__value: Collection[VectorElementType] = value if value is not None else []
        print('CPU Vector initiated')

    def __len__(self) -> int:
        return len(self.__value)

    def __add__(self, other: VectorInterface[VectorElementType]) -> CPUVector[VectorElementType]:
        return CPUVector([i + j for i, j in zip(self.value, other.value) if getattr(other, 'is_cpu')])

    @property
    def value(self) -> Collection[VectorElementType]:
        return self.__value

    @property
    def is_cpu(self) -> bool:
        return True


class GPUVector(VectorInterface[VectorElementType]):

    def __init__(self, value: Optional[Collection[VectorElementType]] = None) -> None:
        self.__value: Collection[VectorElementType] = value if value is not None else []
        print('GPU Vector initiated')

    def __len__(self) -> int:
        return len(self.value)

    def __add__(self, other: VectorInterface[VectorElementType]) -> GPUVector[VectorElementType]:
        return GPUVector([i + j for i, j in zip(self.value, other.value) if getattr(other, 'is_gpu')])

    @property
    def value(self) -> Collection[VectorElementType]:
        return self.__value

    @property
    def is_gpu(self) -> bool:
        return True


def vector(element_type: type, gpu: bool = False) -> Type[VectorInterface[VectorElementType]]:
    return CPUVector[element_type] if not gpu else GPUVector[element_type]
