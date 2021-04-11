from __future__ import annotations

import unittest


class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs) -> Singleton:
        if Singleton.__instance is None:
            Singleton.__instance = super().__new__(cls, *args, **kwargs)
        print("creating memory for instance")
        return Singleton.__instance


class MyTestCase(unittest.TestCase):

    def test_instance_creation(self):
        s_1 = Singleton()
        # self.assertTrue(s_1 is not None)
        del s_1


if __name__ == '__main__':
    unittest.main()
