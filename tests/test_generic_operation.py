__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2020"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from unittest import TestCase
from generic_operation import MathOperation, BinaryOperation, UnaryOperation


class TestGenericOperation(TestCase):

    def setUp(self) -> None:
        self.__int_adder: MathOperation[int] = BinaryOperation('Integer Adder', lambda x, y: x+y)
        self.__int_square: MathOperation[int] = UnaryOperation('Integer Square', lambda x: x**2)

    def test_int_adder(self) -> None:
        sum_result = self.__int_adder(1, 2)
        self.assertEqual(sum_result, 3)

    def test_int_adder_args_mismatch(self) -> None:
        with self.assertRaises(KeyError):
            self.__int_adder(1, 2, 3)

    def test_int_square(self) -> None:
        square_result = self.__int_square(3)
        self.assertEqual(square_result, 9)

    def test_int_square_args_mismatch(self) -> None:
        with self.assertRaises(KeyError):
            self.__int_square(1, 2)

    def tearDown(self) -> None:
        del self.__int_adder
        del self.__int_square
