from __future__ import annotations

import unittest
from typing import Any


class SingletonPattern:

    def __init__(self, cls: type) -> None:
        self.__class = cls
        self.__instance = None

    def __call__(self, *args, **kwargs) -> Any:
        if not self.__instance:
            self.__instance = self.__class(*args, **kwargs)
        return self.__instance


@SingletonPattern
class SingletonTest:
    pass


class SingletonTests(unittest.TestCase):

    def test_same_instance(self):
        self.assertTrue(SingletonTest() is SingletonTest())

    def test_singleton_pattern(self):
        @SingletonPattern  # SingletonPattern(SingletonPattClass)
        class SingletonPattClass:
            def __init__(self, n):
                self.n = n

        self.assertTrue(SingletonPattClass(1) is SingletonPattClass(2))  # SingletonPattern(SingletonPattClass)()
        SingletonPattClass()
        self.assertEqual(SingletonPattClass(3).n, 1)


if __name__ == '__main__':
    unittest.main()
