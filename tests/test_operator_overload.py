__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Sep 2020"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from unittest import TestCase
from operator_overload import MyInteger


class TestOperatorOverloading(TestCase):

    def setUp(self) -> None: pass

    def test_init_integer(self) -> None:
        a_int: MyInteger = MyInteger(3)
        self.assertTrue(a_int.value == 3)

    def test_less_than(self) -> None:
        a_int: MyInteger = MyInteger(3)
        another_int: MyInteger = MyInteger(4)
        self.assertTrue(a_int < another_int)

    def test_greater_than(self) -> None:
        a_int: MyInteger = MyInteger(3)
        another_int: MyInteger = MyInteger(2)
        self.assertTrue(a_int > another_int)

    def test_equal(self) -> None:
        a_int: MyInteger = MyInteger(3)
        another_int: MyInteger = MyInteger(3)
        self.assertTrue(a_int == another_int)

    def test_not_equal(self) -> None:
        a_int: MyInteger = MyInteger(3)
        another_int: MyInteger = MyInteger(2)
        self.assertTrue(a_int != another_int)

    def tearDown(self) -> None: pass

