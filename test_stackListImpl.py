__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "Jul 2019"
__email__ = "bilaleluneis@gmail.com, foundwonder@gmail.com"

from unittest import TestCase
from object_stack_impl import *
import logging as log


class TestStackListImpl(TestCase):

    __stack_inheritance: StackListImpl = StackListImpl()
    __stack_composition: StackListCompoImpl = StackListCompoImpl()

    @classmethod
    def setUpClass(cls):
        log.basicConfig(level=log.INFO)

    def setUp(self):
        pass

    def test00_validate_instance_creation(self):
        self.assertTrue(TestStackListImpl.__stack_inheritance.size == 0)
        self.assertTrue(TestStackListImpl.__stack_composition.size == 0)

    def test01_name(self):
        self.assertEqual('StackListImpl []', str(TestStackListImpl.__stack_inheritance))
        self.assertEqual('StackListCompoImpl []', str(TestStackListImpl.__stack_composition))

    def test02_push_empty(self):
        test_stack_inheritance = TestStackListImpl.__stack_inheritance
        test_stack_composition = TestStackListImpl.__stack_composition
        test_stack_inheritance.push(1)
        test_stack_composition.push(1)
        self.assertEqual('StackListImpl [1]', str(test_stack_inheritance))
        self.assertEqual('StackListCompoImpl [1]', str(test_stack_composition))

    def test03_push_non_empty(self):
        test_stack_inheritance = TestStackListImpl.__stack_inheritance
        test_stack_composition = TestStackListImpl.__stack_composition
        test_stack_inheritance.push(2)
        test_stack_composition.push(2)
        self.assertEqual('StackListImpl [1, 2]', str(test_stack_inheritance))
        self.assertEqual('StackListCompoImpl [1, 2]', str(test_stack_composition))

    def test04_pop_non_empty(self):
        test_stack_inheritance = TestStackListImpl.__stack_inheritance
        test_stack_composition = TestStackListImpl.__stack_composition
        popped_value_inheritance = test_stack_inheritance.pop()
        popped_value_composition = test_stack_composition.pop()
        self.assertEqual(popped_value_inheritance, 2)
        self.assertEqual(popped_value_composition, 2)
        self.assertEqual(test_stack_inheritance.size, 1)
        self.assertEqual(test_stack_composition.size, 1)
        self.assertEqual('StackListImpl [1]', str(test_stack_inheritance))
        self.assertEqual('StackListCompoImpl [1]', str(test_stack_composition))

    def test05_pop_empty(self):
        test_stack_inheritance = TestStackListImpl.__stack_inheritance
        test_stack_composition = TestStackListImpl.__stack_composition
        test_stack_inheritance.pop()
        test_stack_composition.pop()
        popped_value_inheritance = test_stack_inheritance.pop()
        popped_value_composition = test_stack_composition.pop()
        self.assertEqual(popped_value_inheritance, None)
        self.assertEqual(popped_value_composition, None)
        self.assertEqual(test_stack_inheritance.size, 0)
        self.assertEqual(test_stack_composition.size, 0)
        self.assertEqual('StackListImpl []', str(test_stack_inheritance))
        self.assertEqual('StackListCompoImpl []', str(test_stack_composition))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
