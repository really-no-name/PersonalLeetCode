#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2133.py
作者: Bolun Xu
创建日期: 2025/4/7
版本: 1.0
描述: 检查是否每一行每一列都包含全部整数。
时间复杂度： O(N^2)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        def check(m: List[List[int]]) -> bool:
            n = len(m)
            for row in m:
                if len(Counter(row)) == n:
                    continue
                else:
                    return False
            return True

        return check(matrix) and check(list(map(list, zip(*matrix))))


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkValid([[1,2,3],[3,1,2],[2,3,1]]))