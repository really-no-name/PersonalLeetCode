#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1522.py
作者: Bolun Xu
创建日期: 2025/3/3
版本: 1.0
描述: N 叉树的直径。
时间复杂度： O(N)
空间复杂度： O(N)
"""

from typing import Optional, List


# 定义 N 叉树的节点类
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        计算 N 叉树的直径
        :param root: N 叉树的根节点
        :return: 树的直径长度
        """
        self.diameter_length = 0  # 用于存储直径的长度

        def dfs(node: 'Node') -> int:
            """
            深度优先搜索，计算每个节点的深度
            :param node: 当前节点
            :return: 当前节点的深度
            """
            if not node:
                return 0

            max_depth1 = max_depth2 = 0  # 记录当前节点的最大深度和第二大深度

            for child in node.children:
                depth = dfs(child)  # 递归计算子节点的深度
                if depth > max_depth1:
                    max_depth2 = max_depth1
                    max_depth1 = depth
                elif depth > max_depth2:
                    max_depth2 = depth

            # 更新直径长度
            self.diameter_length = max(self.diameter_length, max_depth1 + max_depth2)

            # 返回当前节点的最大深度
            return max_depth1 + 1

        dfs(root)  # 从根节点开始 DFS
        return self.diameter_length


# 调试输出
if __name__ == "__main__":
    # 示例 N 叉树
    #       1
    #     / | \
    #    2  3  4
    #   / \     \
    #  5   6     7
    #       \
    #        8
    root = Node(1, [
        Node(2, [
            Node(5),
            Node(6, [
                Node(8)
            ])
        ]),
        Node(3),
        Node(4, [
            Node(7)
        ])
    ])

    solution = Solution()
    print("树的直径长度:", solution.diameter(root))  # 输出: 树的直径长度: 5
