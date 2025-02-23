#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 转置矩阵。
时间复杂度： O(N^2)
空间复杂度： O(N^2)
执行用时： 0 ms
消耗内存： 18.41 mb
"""
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))


if __name__ == '__main__':
    solution = Solution()
    print(solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
