__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Nov 2020"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from unittest import TestCase
from linked_list import SinglyLinkedList


class TestSinglyLinkedList(TestCase):

    def setUp(self) -> None:
        self.__a_linked_list: SinglyLinkedList[int] = SinglyLinkedList(3)

    def test_insert(self) -> None:
        self.__a_linked_list.insert(5)
        self.assertEqual(len(self.__a_linked_list), 2)

    def test_for_loop(self) -> None:
        self.__a_linked_list.insert(5)
        self.__a_linked_list.insert(7)
        self.__a_linked_list.insert(9)
        for node in self.__a_linked_list:
            print(node)
        print(self.__a_linked_list)

    def test_len(self) -> None:
        self.assertEqual(len(self.__a_linked_list), 1)
        self.__a_linked_list.insert(5)
        self.__a_linked_list.insert(7)
        self.__a_linked_list.insert(9)
        self.assertEqual(len(self.__a_linked_list), 4)

    def test_contains(self) -> None:
        self.__a_linked_list.insert(5)
        self.assertEqual(self.__a_linked_list.contains(3), True)
        self.assertEqual(self.__a_linked_list.contains(7), False)

    def test_delete(self) -> None:
        self.__a_linked_list.insert(5)
        self.__a_linked_list.insert(7)
        self.__a_linked_list.insert(5)
        self.__a_linked_list.insert(9)  # [3, 5, 7, 5, 9]
        self.__a_linked_list.delete(9)
        print(self.__a_linked_list)

    def test_delete_exception(self) -> None:
        with self.assertRaises(Exception):
            self.__a_linked_list.delete(3)

    def tearDown(self) -> None:
        del self.__a_linked_list

