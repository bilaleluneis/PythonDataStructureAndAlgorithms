from __future__ import annotations

__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2018"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from typing import TypeVar, SupportsInt, Optional
from abstract_array import AbstractArray, ArrayIndexOutOfBoundError

T = TypeVar("T", int, bool, SupportsInt)


class InvalidTypeError(Exception):
    pass


class TreeNode:
    def __init__(self, uid: int, a_value: T) -> None:
        self.__uid: Optional[int] = None
        self.__value: Optional[T] = None
        self.__left_child_node: Optional[TreeNode] = None
        self.__right_child_node: Optional[TreeNode] = None
        self.value = a_value
        self.id = uid

    def __repr__(self) -> str:
        return "Node(id={}, value={})".format(self.id, self.value)

    @property
    def value(self) -> T:
        if type(self.__value) is int:
            return int(self.__value)
        else:  # must be a boolean type
            return bool(self.__value)

    @value.setter
    def value(self, new_value: T) -> None:
        if type(new_value) is int:
            self.__value = int(new_value)
        elif type(new_value) is bool:
            self.__value = bool(new_value)
        else:
            raise InvalidTypeError("The type of input value is invalid.")

    @property
    def id(self) -> int:
        return int(self.__uid)

    @id.setter
    def id(self, new_id: int) -> None:
        if type(new_id) is int:
            self.__uid = int(new_id)
        else:
            raise InvalidTypeError("The type of input value is invalid.")

    @property
    def left_child(self) -> Optional[TreeNode]:
        return self.__left_child_node

    @property
    def right_child(self) -> Optional[TreeNode]:
        return self.__right_child_node

    @left_child.setter
    def left_child(self, node: Optional[TreeNode]) -> None:
        if node is None:
            self.__left_child_node = None
        else:
            self.__left_child_node = TreeNode(node.id, node.value)

    @right_child.setter
    def right_child(self, node: Optional[TreeNode]) -> None:
        if node is None:
            self.__right_child_node = None
        else:
            self.__right_child_node = TreeNode(node.id, node.value)

    def insert_child_node(self, node: Optional[TreeNode]) -> None:
        if node is None:
            self.left_child = None
            self.right_child = None
        elif node.id <= self.id:
            self.left_child = node
        else:
            self.right_child = node


class ArrayTreeImpl(AbstractArray):

    def __init__(self):
        super().__init__()
        self.__node: Optional[TreeNode] = None

    def __str__(self) -> str:
        description: str = "{} [".format(self._class_name)

        if self.size > 0:
            for i in range(self.size):
                current_value = self.get(i)
                description += "{}, ".format(current_value)

            description = description[:-2]
        description += "]"

        return description

    @property
    def size(self) -> int:
        return self.__offspring_counter(self.__node)

    def get(self, at_index: int) -> Optional[int]:  # returns an int or None
        if at_index < 0 or at_index >= self.size:
            return None
        else:
            return self.__get_node(at_index).value

    def remove(self, at_index: Optional[int] = None) -> Optional[int]:
        # pass
        resolved_index: Optional[int] = at_index

        if at_index is None:
            resolved_index = self.size - 1

        value_at_index: Optional[int] = self.get(resolved_index)

        if value_at_index is not None:
            node_to_remove = self.__get_node(resolved_index)
            # cut right branch, cut left branch, right branch copied to current node,
            # find the smallest idex from current node, insrt left branch
            right_branch = node_to_remove.right_child
            left_branch = node_to_remove.left_child

            if right_branch is not None:
                self.__deep_copy_to_node(right_branch, self.__get_node(resolved_index))
                self.__shift_id_from_index_pass_node(self.__node, resolved_index, -1)
                # self.__get_node(resolved_index).id = right_branch.id
                # resolved_index = right_branch.id
                # self.__get_node(resolved_index).value = right_branch.value
                # self.__get_node(resolved_index).left_child = right_branch.left_child  # FIXME
                # self.__get_node(resolved_index).right_child = right_branch.right_child  # FIXME
                # node_to_remove.id = right_branch.id
                # node_to_remove.value = right_branch.value
                # node_to_remove.right_child = right_branch.right_child
                # node_to_remove.left_child = right_branch.left_child

                if left_branch is not None:
                    self.__find_the_node_with_smallest_index(self.__get_node(resolved_index)).left_child = left_branch
                    left_branch_index: int = left_branch.id

                    # node_to_insert_left_branch = self.__find_the_node_with_smallest_index(self.__get_node(resolved_index))
                    # node_to_insert_left_branch.left_child = left_branch
                    self.__deep_copy_to_node(left_branch, self.__get_node(left_branch_index))
            else:
                if left_branch is None:  # right and left branch both None
                    self.__set_node_to_none(node_to_remove)
                else: # right is None, left is not
                    self.__deep_copy_to_node(left_branch, self.__get_node(resolved_index))
                    # self.__get_node(resolved_index).id = left_branch.id
                    # resolved_index = left_branch.id
                    # self.__get_node(resolved_index).value = left_branch.value
                    # self.__get_node(resolved_index).left_child = left_branch.left_child
                    # self.__get_node(resolved_index).right_child = left_branch.right_child



        return value_at_index

    def set(self, value: int, at_index: int) -> None:
        node_to_set = self.__get_node(at_index)
        if node_to_set is not None:
            node_to_set.value = value

    def insert(self, value: int, at_index: Optional[int] = None) -> None:
        resolved_index: Optional[int] = at_index

        if at_index is None:
            resolved_index: int = int(self.size)

        if resolved_index in range(self.size + 1):  # if index = size, put it at the end.
            if self.__node is None:  # empty
                self.__node = TreeNode(resolved_index, value)
            else:
                self.__shift_id_from_index_pass_node(self.__node, resolved_index, 1)
                self.__insert_from_node(self.__node, resolved_index, value)

        else:
            class_name: str = self._class_name
            error: str = "{}._insert[{}]={} Failed, index {} is invalid!".format(class_name, at_index, value, at_index)
            raise ArrayIndexOutOfBoundError(error)

    """ utility methods """

    def __offspring_counter(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        else:
            return self.__offspring_counter(node.left_child) + self.__offspring_counter(node.right_child) + 1

    def __get_node(self, at_index: int) -> Optional[TreeNode]:
        root_node = self.__node
        while root_node is not None:
            if root_node.id == at_index:
                return root_node
            elif root_node.id < at_index:
                root_node = root_node.right_child
            else:
                root_node = root_node.left_child
        return root_node

    def __shift_id(self, from_index: int, number: int) -> None:  # shift id of index and its right offspring
        root_node = self.__node
        while root_node is not None:
            if from_index <= root_node.id:
                root_node.id += number
                if root_node.right_child is not None:
                    self.__offspring_shift_id_from_node(root_node.right_child, number)
                root_node = root_node.left_child
            else:
                root_node = root_node.right_child

    def __shift_id_from_index_pass_node(self, node: TreeNode, from_index: int, number: int) -> None:
        if from_index <= node.id:
            node.id += number
            if node.right_child is not None:
                self.__offspring_shift_id_from_node(node.right_child, number)
            if node.left_child is not None:
                self.__shift_id_from_index_pass_node(node.left_child, from_index, number)
        else:
            if node.right_child is not None:
                self.__shift_id_from_index_pass_node(node.right_child, from_index, number)

    def __offspring_shift_id_from_node(self, node: Optional[TreeNode], number: int) -> None:
        if node is not None:
            node.id += number
            self.__offspring_shift_id_from_node(node.left_child, number)
            self.__offspring_shift_id_from_node(node.right_child, number)

    def __insert_from_node(self, node: TreeNode, index: int, value: int):
        if index < node.id:
            if node.left_child is None:
                node.left_child = TreeNode(index, value)
            else:
                self.__insert_from_node(node.left_child, index, value)
        else:
            if node.right_child is None:
                node.right_child = TreeNode(index, value)
            else:
                self.__insert_from_node(node.right_child, index, value)

    def __find_node_to_insert(self, at_index):
        root_node = self.__node
        while root_node is not None:
            if at_index <= root_node.id:
                if root_node.left_child is None:
                    return root_node
                else:
                    root_node = root_node.left_child
            else:
                if root_node.right_child is None:
                    return root_node
                else:
                    root_node = root_node.right_child

    def __get_parent_node(self, at_index: int) -> Optional[TreeNode]:
        root_node = self.__node
        if self.size == 0 or at_index == root_node.id:
            return None
        else:
            if at_index < root_node.id:
                if at_index == root_node.left_child.id:
                    return root_node
                else:
                    root_node = root_node.left_child
            else:
                if at_index == root_node.right_child.id:
                    return root_node
                else:
                    root_node = root_node.right_child

    def __get_parent_node_at_index_pass_node(self, at_index: int, from_node: TreeNode) -> Optional[TreeNode]:
        if at_index == from_node.id:
            return None
        elif at_index < from_node.id:
            if at_index == from_node.left_child.id:
                return from_node
            else:
                return self.__get_parent_node_at_index_pass_node(at_index, from_node.left_child)
        else:
            if at_index == from_node.right_child.id:
                return from_node
            else:
                return self.__get_parent_node_at_index_pass_node(at_index, from_node.right_child)

    def __set_node_to_none(self, node: Optional[TreeNode]):
        if node is None:
            return
        elif node is self.__node:
            node.__init__(None, None) # FIXME: set to None
        else:
            parent_node = self.__get_parent_node_at_index_pass_node(node.id, self.__node)
            if node.id < parent_node.id:
                parent_node.left_child = None
            else:
                parent_node.right_child = None

    # def __deep_copy_to_an_empty_node(self, copy_node: Optional[TreeNode], copy_target: Optional[TreeNode]) -> None:
    #     if copy_node is not None:
    #         copy_target.id = copy_node.id
    #         copy_target.value = copy_node.value
    #         self.__deep_copy_to_an_empty_node(copy_node.left_child, copy_target.left_child)
    #         self.__deep_copy_to_an_empty_node(copy_target.right_child, copy_target.right_child)

    def __deep_copy_to_node(self, copy_node: Optional[TreeNode], target_node: Optional[TreeNode]) -> None:
        if copy_node is not None:
            target_node = TreeNode(target_node.id, copy_node.value)
            if copy_node.left_child is None:
                target_node.left_child = None
            else:
                target_node.left_child = copy_node.left_child
                self.__deep_copy_to_node(copy_node.left_child, target_node.left_child)

            if copy_node.right_child is None:
                target_node.right_child = None
            else:
                self.__deep_copy_to_node(copy_node.right_child, target_node.right_child)

    def __deep_copy_offspring(self, copy_node: Optional[TreeNode], target_node: Optional[TreeNode]) -> None:
        pass


    # def __deep_copy_node(self, target_node: Optional[TreeNode], copy_node: Optional[TreeNode]) -> None:
    #     if copy_node is None:
    #         if target_node is None:
    #             return
    #         else:
    #             parent_node = self.__get_parent_node_at_index_pass_node(target_node.id, self.__node)
    #             # FIXME: if target node is a new node, self.__node would be problematic, could not find.
    #             if parent_node is None:
    #                 self.__set_node_to_none(target_node)
    #             elif target_node.id < parent_node.id:
    #                 parent_node.left_child = None
    #             else:
    #                 parent_node.right_child = None
    #
    #     else: # copy_node is not None
    #         if target_node is not None:
    #             target_node.id = copy_node.id
    #             target_node.value = copy_node.value
    #             if copy_node.left_child is None:
    #                 target_node.left_child = None
    #             else:
    #                 self.__deep_copy_node(target_node.left_child, copy_node.left_child)
    #
    #             if copy_node.right_child is None:
    #                 target_node.right_child = None
    #             else:
    #                 self.__deep_copy_node((target_node.right_child, copy_node.right_child))
    #
    #         else: # target node is None
    #             target_node = TreeNode(copy_node.id, copy_node.value)
    #             self.__deep_copy_node(target_node.left_child, copy_node.left_child)
    #             self.__deep_copy_node(target_node.right_child, copy_node.right_child)

    def __find_the_node_with_smallest_index(self, from_node: Optional[TreeNode]) ->Optional[TreeNode]:
        if from_node is None:
            return None
        elif from_node.left_child is None:
            return from_node
        else:
            self.__find_the_node_with_smallest_index(from_node.left_child)

    # def __shift_direct_children_id(self, node: Optional[TreeNode], number: int):
    #     if node is not None:
    #         if node.left_child is not None:
    #             node.right_child.id += number
    #         if node.right_child is not None:
    #             node.right_child.id += number

    # def __find_parent_node(self, at_index: int) -> Optional[TreeNode]:
    #     root_node = self.__node
    #     if root_node.id == at_index:
    #         return None
    #     else:
    #         while True:
    #             if root_node.id > at_index:
    #                 if root_node.left_child.id == at_index:
    #                     return root_node
    #                 else:
    #                     root_node = root_node.left_child
    #             else:
    #                 if root_node.right_child.id == at_index:
    #                     return root_node
    #                 else:
    #                     root_node = root_node.right_child

    # def __ancester_number(self, node):
    #     if node is self.__node:
    #         return 0
    #     else:
    #         parent_node = self.__find_parent_node(node.id)
    #         return self.__ancester_number(parent_node) + 1

    # def __insert_at_index(self, value, at_index):
    #     root_node = self.__node
    #     possible_nodes_to_insert = {}
    #     while root_node.left_child is not None or root_node.right_child is not None:
    #         if at_index <= root_node.id:
    #             if root_node.left_child is None:
    #                 index = root_node.id
    #                 possible_nodes_to_insert[index] = root_node
    #             else:
    #                 root_node = root_node.right_child
    #         else:
    #             if root_node.right_child is None:
    #                 possible_nodes_to_insert[index] = root_node
    #             else:
    #                 root_node = root_node.left_child
    #
    #     for i in possible_nodes_to_insert:
    #         ancester_number_dic = {}
    #         ancester_number_dic[i] = self.__ancester_number(i)
    #         min_ancester = min(self.__ancester_number(i))

