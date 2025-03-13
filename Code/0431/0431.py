#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0431.py
作者: Bolun Xu
创建日期: 2025/3/13
版本: 1.0
描述: 将 N 叉树编码为二叉树。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import Optional, List

from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


# Codec class to encode and decode N-ary tree to binary tree and vice versa.
class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None

        # Create a binary tree node with the same value as the n-ary tree node
        binary_root = TreeNode(root.val)

        # Encode the first child as the left child of the binary tree node
        if root.children:
            binary_root.left = self.encode(root.children[0])

        # Encode the rest of the children as the right child of the previous encoded node
        current = binary_root.left
        for i in range(1, len(root.children)):
            current.right = self.encode(root.children[i])
            current = current.right

        return binary_root

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None

        # Create an n-ary tree node with the same value as the binary tree node
        nary_root = Node(data.val, [])

        # Decode the left child as the first child of the n-ary tree node
        current = data.left
        while current:
            nary_root.children.append(self.decode(current))
            current = current.right

        return nary_root


# Helper function to print N-ary tree (for testing)
def print_nary_tree(root: Optional[Node], level: int = 0):
    if not root:
        return
    print("  " * level + str(root.val))
    for child in root.children:
        print_nary_tree(child, level + 1)


# Helper function to print binary tree (for testing)
def print_binary_tree(root: Optional[TreeNode], level: int = 0):
    if not root:
        return
    print("  " * level + str(root.val))
    print_binary_tree(root.left, level + 1)
    print_binary_tree(root.right, level + 1)


# Main program to test the Codec
if __name__ == "__main__":
    # Create an example N-ary tree
    #       1
    #     / | \
    #    2  3  4
    #   / \    /|\
    #  5   6  7 8 9
    nary_root = Node(1)
    nary_root.children = [Node(2), Node(3), Node(4)]
    nary_root.children[0].children = [Node(5), Node(6)]
    nary_root.children[2].children = [Node(7), Node(8), Node(9)]

    print("Original N-ary Tree:")
    print_nary_tree(nary_root)

    # Encode the N-ary tree to a binary tree
    codec = Codec()
    binary_root = codec.encode(nary_root)

    print("\nEncoded Binary Tree:")
    print_binary_tree(binary_root)

    # Decode the binary tree back to an N-ary tree
    decoded_nary_root = codec.decode(binary_root)

    print("\nDecoded N-ary Tree:")
    print_nary_tree(decoded_nary_root)
