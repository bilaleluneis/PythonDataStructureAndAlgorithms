from __future__ import annotations

__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Oct 2020"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from generic_operation import MathOperation, BinaryOperation
from typing import Protocol, TypeVar, Type, Optional, Union, Any
from abc import abstractmethod

T = TypeVar('T')
OperationName: Type[str] = str
Operations = dict[OperationName, MathOperation[Any]]


class CalculatorProtocol(Protocol[T]):
    __accumulator: Optional[T]
    __op_queue: list[Union[str, MathOperation[T]]]

    @property
    @abstractmethod
    def accumulator(self) -> T: ...

    @abstractmethod
    def operator(self, op: OperationName) -> None: ...

    @abstractmethod
    def operand(self, param: T) -> None: ...

    @abstractmethod
    def evaluate(self) -> None: ...

    @abstractmethod
    def clear(self) -> None: ...


class SimpleCalculator(CalculatorProtocol[T]):

    def __init__(self, supported_operations: Operations) -> None:
        self.__operations = supported_operations
        self.__accumulator = None
        self.__op_queue: Optional[list[Union[str, MathOperation[T]]]] = []

    @property
    def accumulator(self) -> T:
        return self.__accumulator

    def operator(self, op: OperationName) -> None:
        self.__op_queue.append(self.__operations[op])

    def operand(self, param: T) -> None:
        self.__op_queue.append(param)

    def evaluate(self) -> None:
        self.__accumulator: T = self.__op_queue.pop(0)
        while len(self.__op_queue):
            params: list[T] = [self.accumulator]
            operator: MathOperation[T] = self.__op_queue.pop(0)
            if isinstance(operator, BinaryOperation):
                params.append(self.__op_queue.pop(0))
            self.__accumulator = operator(*params)

    def clear(self) -> None:
        self.__accumulator = None
        self.__op_queue = []
