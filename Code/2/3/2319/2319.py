#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2319.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 判断矩阵是否是一个 X 矩阵。
时间复杂度： O(N^2)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid)):
                print(grid[i][j])
                if i == j or i + j == len(grid) - 1:
                    print('在对角线')
                    if grid[i][j] == 0:
                        return False
                else:
                    print('不在对角线')
                    if grid[i][j] != 0:
                        return False
        return True
