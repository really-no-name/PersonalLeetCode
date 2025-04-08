#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1572.py
作者: Bolun Xu
创建日期: 2025/4/8
版本: 1.0
描述: 矩阵对角线元素的和。
时间复杂度： O(N^2)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        print(n)
        ans = 0
        for i in range(n):
            for j in range(n):
                if i == j and i + j == n - 1:
                    ans += mat[i][i]
                    continue
                if i == j:  # 主对角线
                    print("主对角线", mat[i][j])
                    ans += mat[i][j]
                if i + j == n - 1:
                    print("副对角线", mat[i][j])
                    ans += mat[i][j]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.diagonalSum([[1,2,3],
            [4,5,6],
            [7,8,9]]))