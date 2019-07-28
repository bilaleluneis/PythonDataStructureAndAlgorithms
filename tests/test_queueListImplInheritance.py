__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "Jul 2019"
__email__ = "bilaleluneis@gmail.com, foundwonder@gmail.com"


from unittest import TestCase
from object_queue_impl import *
import logging as log


class TestQueueListImpl(TestCase):

    __queue_inheritance: QueueListImplInheritance = QueueListImplInheritance()
    __queue_composition: QueueListImplComposition = QueueListImplComposition()

    @classmethod
    def setUpClass(cls):
        log.basicConfig(level=log.INFO)

    def setUp(self):
        pass

    def test00_validate_instance_creation(self):
        self.assertTrue(TestQueueListImpl.__queue_inheritance.size == 0)
        self.assertTrue(TestQueueListImpl.__queue_composition.size == 0)
        self.assertEqual('QueueListImplInheritance []', str(TestQueueListImpl.__queue_inheritance))
        self.assertEqual('QueueListImplComposition []', str(TestQueueListImpl.__queue_composition))

    def test01_dequeue_empty(self):
        test_queue_inheritance = TestQueueListImpl.__queue_inheritance
        test_queue_composition = TestQueueListImpl.__queue_composition
        popped_value_inheritance = test_queue_inheritance.dequeue()
        popped_value_composition = test_queue_composition.dequeue()
        self.assertEqual(popped_value_inheritance, None)
        self.assertEqual(popped_value_composition, None)
        self.assertEqual(test_queue_inheritance.size, 0)
        self.assertEqual(test_queue_composition.size, 0)
        self.assertEqual('QueueListImplInheritance []', str(test_queue_inheritance))
        self.assertEqual('QueueListImplComposition []', str(test_queue_composition))

    def test02_enqueue_empty(self):
        test_queue_inheritance = TestQueueListImpl.__queue_inheritance
        test_queue_composition = TestQueueListImpl.__queue_composition
        test_queue_inheritance.enqueue(1)
        test_queue_composition.enqueue(1)
        self.assertEqual('QueueListImplInheritance [1]', str(test_queue_inheritance))
        self.assertEqual('QueueListImplComposition [1]', str(test_queue_composition))

    def test03_enqueue_non_empty(self):
        test_queue_inheritance = TestQueueListImpl.__queue_inheritance
        test_queue_composition = TestQueueListImpl.__queue_composition
        test_queue_inheritance.enqueue(2)
        test_queue_composition.enqueue(2)
        self.assertEqual('QueueListImplInheritance [1, 2]', str(test_queue_inheritance))
        self.assertEqual('QueueListImplComposition [1, 2]', str(test_queue_composition))

    def test04_dequeue_non_empty(self):
        test_queue_inheritance = TestQueueListImpl.__queue_inheritance
        test_queue_composition = TestQueueListImpl.__queue_composition
        popped_value_inheritance = test_queue_inheritance.dequeue()
        popped_value_composition = test_queue_composition.dequeue()
        self.assertEqual(popped_value_inheritance, 1)
        self.assertEqual(popped_value_composition, 1)
        self.assertEqual(test_queue_inheritance.size, 1)
        self.assertEqual(test_queue_composition.size, 1)
        self.assertEqual('QueueListImplInheritance [2]', str(test_queue_inheritance))
        self.assertEqual('QueueListImplComposition [2]', str(test_queue_composition))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
