#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2946.py
作者: Bolun Xu
创建日期: 2025/3/15
版本: 1.0
描述: 循环移位后的矩阵相似检查。
时间复杂度：O(N∗M)
空间复杂度：O(1)
"""
from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k %= len(mat[0])
        return k == 0 or all(r == r[k:] + r[:k] for r in mat)


if __name__ == '__main__':
    solution = Solution()
    print(solution.areSimilar(mat=[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], k=1))
    print(solution.areSimilar(mat=[[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], k=2))
    print(solution.areSimilar([[1, 2]], k=1))
