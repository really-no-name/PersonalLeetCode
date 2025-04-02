#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2427.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 公因子的数目。
时间复杂度： O(Max(A,B))
空间复杂度： O(1)
"""
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factor = min(a, b)
        ans = 0
        while factor > 0:
            if a % factor == 0 and b % factor == 0:
                ans += 1
            factor -=1
        return ans