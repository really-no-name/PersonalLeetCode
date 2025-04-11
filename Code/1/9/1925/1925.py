#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1925.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 统计平方和三元组的数目。
时间复杂度： O(N^2)
空间复杂度： O(1)
"""
import math


class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                c = math.sqrt(a ** 2 + b ** 2)
                if int(c) == c and c <= n:
                    cnt += 2
        return cnt