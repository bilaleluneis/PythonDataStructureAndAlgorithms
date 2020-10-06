__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2020"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from unittest import TestCase
from dictionary import Dictionary
from immutable_types import Immutable, MyKeyType


class TestDictionary(TestCase):

    def setUp(self) -> None:
        self.__custom_dictionary: Dictionary[str, int] = Dictionary[str, int]()
        self.__default_dictionary: dict[str, int] = dict()

    def test_0_initialize_empty_dictionary(self) -> None:
        self.assertTrue(self.__custom_dictionary is not None)
        self.assertTrue(self.__default_dictionary is not None)
        self.assertTrue(len(self.__custom_dictionary) == 0)
        self.assertTrue(len(self.__default_dictionary) == 0)

    def test_1_initialize_non_empty_dictionary(self) -> None:
        self.__default_dictionary = dict([('cat', 3), ('dog', 5)])
        self.__custom_dictionary = Dictionary[str, int]([('cat', 3), ('dog', 5), ('sheep', 7)])
        self.assertEqual(len(self.__custom_dictionary), 3)
        self.assertEqual(len(self.__default_dictionary), 2)

    def test_2_set_new_item(self) -> None:
        self.__default_dictionary['cat'] = 3
        self.__custom_dictionary['dog'] = 4
        self.assertEqual(len(self.__custom_dictionary), 1)
        self.assertEqual(len(self.__default_dictionary), 1)

    def test_3_set_existing_item(self) -> None:
        self.__default_dictionary = dict([('cat', 3), ('dog', 5)])
        self.__custom_dictionary = Dictionary[str, int]([('cat', 3), ('dog', 5), ('sheep', 7)])
        self.__default_dictionary['cat'] = 300
        self.__custom_dictionary['dog'] = 400
        self.assertEqual(self.__custom_dictionary['dog'], 400)
        self.assertEqual(self.__default_dictionary['cat'], 300)

    def test_4_is_key_in_dict(self) -> None:
        self.__default_dictionary = dict([('cat', 3), ('dog', 5)])
        self.__custom_dictionary = Dictionary[str, int]([('cat', 3), ('dog', 5), ('sheep', 7)])
        self.assertTrue('cat' in self.__default_dictionary)
        self.assertFalse('sheep' in self.__default_dictionary)
        self.assertTrue('cat' in self.__custom_dictionary)
        self.assertFalse('bird' in self.__custom_dictionary)

    def test_5_get_key_list(self) -> None:
        self.__default_dictionary = dict([('cat', 3), ('dog', 5)])
        self.__custom_dictionary = Dictionary[str, int]([('cat', 3), ('dog', 5), ('sheep', 7)])
        self.assertEqual(len(self.__default_dictionary.keys()), 2)
        self.assertEqual(len(self.__custom_dictionary.keys()), 3)

    def test_6_items(self) -> None:
        self.__default_dictionary = dict([('cat', 3), ('dog', 5)])
        self.__custom_dictionary = Dictionary[Immutable[list[str]], int]([(MyKeyType(['1']), 3), (MyKeyType(['2']), 5)])
        keys = self.__default_dictionary.keys()
        items = self.__default_dictionary.items()

    def tearDown(self) -> None:
        del self.__custom_dictionary
        del self.__default_dictionary
