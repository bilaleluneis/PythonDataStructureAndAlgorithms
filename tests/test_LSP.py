__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2020"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from unittest import TestCase
from LSP import Number, Integer, Float


class TestNumber(TestCase):

    def setUp(self) -> None: pass

    def test_init_Number(self) -> None:
        with self.assertRaises(TypeError):
            vector_interface = Number()  # type: ignore

    def test_init_integer(self) -> None:
        number: Number[int] = Integer(3)
        self.assertEqual(number.value, 3)

    def test_add_integer(self) -> None:
        integer_1: Number[int] = Integer(4)
        integer_2: Number[int] = Integer(5)
        integer_sum: Number[int] = integer_1 + integer_2
        self.assertEqual(integer_sum.value, 9)

    def test_add_float(self) -> None:
        float_1: Number[float] = Float(4.0)
        float_2: Number[float] = Float(5.0)
        float_sum: Number[float] = float_1 + float_2
        self.assertEqual(float_sum.value, 9.0)

    def test_add_int_float(self) -> None:
        a_integer: Number[int] = Integer(4)
        a_float: Number[float] = Float(5.0)
        number_sum = a_integer + a_float

    def tearDown(self) -> None: pass
