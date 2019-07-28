__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "July 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from unittest import TestCase
import logging as log
from abstract_array import ArrayNodeImpl


class TestArrayNodeImpl(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        log.basicConfig(level=log.INFO)

    def setUp(self) -> None:
        self.node_array: ArrayNodeImpl = ArrayNodeImpl()

    def test_size(self):
        self.assertTrue(self.node_array.size == 0)

    def test_get(self):
        self.fail()

    def test_remove(self):
        self.fail()

    def test_set(self):
        self.fail()

    def test_insert(self):
        self.fail()

    def tearDown(self) -> None:
        self.array = None

    @classmethod
    def tearDownClass(cls) -> None:
        pass
