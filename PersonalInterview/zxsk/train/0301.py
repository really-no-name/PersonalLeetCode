#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0301.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 2)

    def update(self, index, value):
        while index <= self.n:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

def count_eight_diagrams(n, A):
    MAX_A = 32768
    left_tree = FenwickTree(MAX_A)
    right_tree = FenwickTree(MAX_A)

    # 初始化右边树状数组
    for a in A:
        right_tree.update(a, 1)

    result = 0
    for j in range(n):
        mid = A[j]
        # 当前值从右边去掉，表示作为中心点时它不在右边了
        right_tree.update(mid, -1)

        left_count = left_tree.query(mid - 1)
        right_count = right_tree.query(mid - 1)

        result += left_count * right_count

        # 当前值加入左边
        left_tree.update(mid, 1)

    return result

# 主程序
if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    print(count_eight_diagrams(n, A))