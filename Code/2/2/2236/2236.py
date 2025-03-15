#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 判断根结点是否等于子结点之和。
时间复杂度： O(N)
空间复杂度： O(H)

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root and root.left and root.right:
            return root.val == root.left.val + root.right.val
        return False


# 测试主函数
def main():
    # 测试用例 1: 根节点值等于左右子节点值之和
    # 构建二叉树:
    #     10
    #    /  \
    #   4    6
    root1 = TreeNode(10)
    root1.left = TreeNode(4)
    root1.right = TreeNode(6)
    solution = Solution()
    print(solution.checkTree(root1))  # 预期输出: True

    # 测试用例 2: 根节点值不等于左右子节点值之和
    # 构建二叉树:
    #     10
    #    /  \
    #   3    6
    root2 = TreeNode(10)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    print(solution.checkTree(root2))  # 预期输出: False

    # 测试用例 3: 根节点或子节点缺失
    # 构建二叉树:
    #     10
    #    /
    #   4
    root3 = TreeNode(10)
    root3.left = TreeNode(4)
    print(solution.checkTree(root3))  # 预期输出: False

    # 测试用例 4: 只有根节点
    # 构建二叉树:
    #     10
    root4 = TreeNode(10)
    print(solution.checkTree(root4))  # 预期输出: False


if __name__ == "__main__":
    main()
