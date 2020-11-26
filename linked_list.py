from __future__ import annotations

__author__ = "Bilal El Uneis and Jieshu Wang"
__since__ = "Nov 2020"
__email__ = "bilaleluneis@gmail.com and foundwonder@gmail.com"

from typing import Protocol, TypeVar, Type, Optional, Union, Any, Collection, OrderedDict, Tuple, Generic, Generator, cast
from dataclasses import dataclass

T = TypeVar('T', int, float)


class SinglyLinkedList(Generic[T]):

    @dataclass
    class _Node(Generic[T]):
        value: Optional[T] = None
        linked_node: Optional[SinglyLinkedList._Node[T]] = None

        def __repr__(self):
            return f'Node({self.value})'

    def __init__(self, root_value: T):
        self._root_node: SinglyLinkedList._Node[T] = self._Node(value=root_value)

    def __len__(self):
        return len([1 for node in self])

    def __iter__(self) -> Generator[T]:
        for node in self._node_generator():
            yield node.value

    def __repr__(self) -> str:
        return '->'.join([str(node) for node in self]) + '->()'

    def insert(self, inserting_value: T) -> None:
        inserting_node: SinglyLinkedList._Node[T] = self._Node(value=inserting_value)
        for node in self._node_generator():
            if node.linked_node is None:
                node.linked_node = inserting_node

    def contains(self, value: T) -> bool:
        return self._find_the_first_node_with_value(value) is not None

    def delete(self, value: T) -> None:
        deleting_node = self._find_the_first_node_with_value(value)
        parent_node = self._find_parent_node(value)
        child_node: Optional[SinglyLinkedList._Node[T]] = deleting_node.linked_node
        if parent_node is None:  # if the deleting node is root
            if child_node is None:
                raise Exception('Cannot delete because only one node exists.')
            else:
                self._root_node = child_node  # connecting the child node to the root node
        else:
            parent_node.linked_node = child_node
        del deleting_node

    """Helper Methods"""

    def _find_the_first_node_with_value(self, value: T) -> Union[SinglyLinkedList._Node[T], None]:
        for node in self._node_generator():
            if node.value == value:
                return node
        return None

    def _find_parent_node(self, value: T) -> Union[SinglyLinkedList._Node[T], None]:
        """
        :param value: the value of the node whose parent is being looked for.
        :return: a) None, if no parent exists, meaning it's the value of root node; b) the parent node.
        """
        if self._root_node.value == value:
            return None
        for node in self._node_generator():
            if node.linked_node.value == value:
                return node

    def _node_generator(self) -> Generator[_Node[T]]:
        """
        a generator that yields instances of _Node[T] object,
        used internally for accessing protected class _Node[T]
        :return:
        """
        current_node = self._root_node
        while current_node.linked_node is not None:
            yield current_node
            current_node = current_node.linked_node
        yield current_node

