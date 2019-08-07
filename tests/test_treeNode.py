__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "Agu 2019"
__email__ = "bilaleluneis@gmail.com"

from unittest import TestCase
from tree_node_array import TreeNode, InvalidTypeError
from typing import Optional


class TestNode(TestCase):
    __node: Optional[TreeNode] = None

    @classmethod
    def setUpClass(cls):
        cls.__node = TreeNode(uid=0, a_value=1)

    def setUp(self):
        pass

    def test_0_verify_node_created(self):
        self.assertTrue(TestNode.__node is not None)
        self.assertTrue(TestNode.__node.value == 1)
        self.assertEqual(TestNode.__node.id, 0)

    def test_1_init_child_node(self):
        TestNode.__node.insert_child_node(TreeNode(uid=1, a_value=5))
        TestNode.__node.insert_child_node(TreeNode(uid=0, a_value=6))  # (0, 1), (0, 6), (1, 5)
        self.assertIsNotNone(TestNode.__node.left_child)
        self.assertIsNotNone(TestNode.__node.right_child)
        self.assertEqual(TestNode.__node.left_child.id, 0)
        self.assertEqual(TestNode.__node.right_child.value, 5)

    def test_2_update_node_value(self):
        # update the parent node value
        TestNode.__node.value = 3  # (0, 3), (0, 6), (1, 5)
        TestNode.__node.left_child.value = 4  # (0, 3), (0, 4), (1, 5)
        self.assertEqual(TestNode.__node.value, 3)
        self.assertEqual(TestNode.__node.left_child.value, 4)

    def test_3_update_node_id(self):
        # update the parent node id
        TestNode.__node.id = 1
        TestNode.__node.right_child.id = (2)  #  (1, 3), (0, 4), (2, 5)
        self.assertEqual(TestNode.__node.id, 1)
        self.assertEqual(TestNode.__node.right_child.id, 2)

    def test_4_raise_error_on_invalid_id(self):
        with self.assertRaises(InvalidTypeError):
            TestNode.__node.id = "True"

    def test_5_raise_error_on_invalid_value(self):
        with self.assertRaises(InvalidTypeError):
            TestNode.__node.value = "True"

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        del cls.__node
