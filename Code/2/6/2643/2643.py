#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2643.py
作者: Bolun Xu
创建日期: 2025/3/22
版本: 1.0
描述: 一最多的行。
时间复杂度： O(N∗M)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_num = 0
        max_index = 0
        for i, m in enumerate(mat):
            if m.count(1) > max_num:
                max_num = m.count(1)
                max_index = i
        return [max_index, max_num]


if __name__ == '__main__':
    sol = Solution()
    print(sol.rowAndMaximumOnes([[0, 0, 0], [0, 1, 1]]))
