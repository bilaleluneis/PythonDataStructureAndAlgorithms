__author__ = "Bilal El Uneis"
__since__ = "July 2019"
__email__ = "bilaleluneis@gmail.com"

from unittest import TestCase
from node import Node, NodeAlreadyInitializedError
from typing import Optional


class TestNode(TestCase):

    __node: Optional[Node] = None

    @classmethod
    def setUpClass(cls):
        cls.__node = Node(value=1, uid=0)

    def setUp(self):
        pass

    def test_0_verify_node_created(self):
        self.assertTrue(TestNode.__node is not None)
        self.assertTrue(TestNode.__node.value == 1)
        self.assertEqual(TestNode.__node.id, 0)

    def test_1_init_child_node(self):
        TestNode.__node.init_child(uid=1, value=5)
        self.assertIsNotNone(TestNode.__node.child)
        self.assertEqual(TestNode.__node.child.id, 1)
        self.assertEqual(TestNode.__node.child.value, 5)

    def test_2_raise_exception_on_reinit_child(self):
        self.assertRaises(NodeAlreadyInitializedError, TestNode.__node.init_child, 2, 6)

    def test_3_update_nodes_values(self):
        # update the parent node id
        original_node_id: int = TestNode.__node.id
        TestNode.__node.id = int(original_node_id + 1)
        self.assertEqual(TestNode.__node.id, original_node_id + 1)

        # update the child  node id
        original_child_node_id: int = TestNode.__node.child.id
        TestNode.__node.child.id = int(original_child_node_id + 1)
        self.assertEqual(TestNode.__node.child.id, original_child_node_id + 1)

        # upate the parent node value
        origianl_node_value: int = TestNode.__node.value
        TestNode.__node.value = int(TestNode.__node.child.value)
        self.assertNotEqual(TestNode.__node.value, origianl_node_value)
        self.assertEqual(TestNode.__node.value, TestNode.__node.child.value)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        del cls.__node
