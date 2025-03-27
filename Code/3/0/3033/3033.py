#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3033.py
作者: Bolun Xu
创建日期: 2025/3/27
版本: 1.0
描述: 修改矩阵。
时间复杂度： O(Mn)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        max_value = [0] * n
        for i in range(m):
            for j in range(n):
                max_value[j] = max(max_value[j], matrix[i][j])
        print(max_value)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_value[j]

        return matrix


if __name__ == '__main__':
    sol = Solution()
    print(sol.modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]]))