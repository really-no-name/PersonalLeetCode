#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 丑数。
时间复杂度： O(Logn)
空间复杂度： O(1)
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n > 0:
            while n % 5 == 0:
                n //= 5
            while n % 3 == 0:
                n //= 3
            if n & (n - 1) == 0:
                return True
        return False
