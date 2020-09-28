__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Sep 2020"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from typing import List, Tuple, Sequence
from unittest import TestCase
import numpy as np
from generic_search_function import linear_search
from vector import CPUVector


class TestGenericLinearSearch(TestCase):

    def setUp(self) -> None:
        self.__list: List[int] = [1, 2, 3]
        self.__tuple: Tuple[int, int, int] = (1, 2, 3)

    def test_search_non_existing_item(self) -> None:
        # using List
        self.assertTrue(linear_search(self.__list, 4) is None)
        self.assertTrue(linear_search(self.__tuple, 4) is None)
        # using Array

        # using custom Type

    def test_search_existing_item(self) -> None:
        self.assertTrue(linear_search(self.__list, 2) == 1)
        self.assertTrue(linear_search(self.__tuple, 2) == 1)

    def tearDown(self) -> None:
        del self.__list
        del self.__tuple
