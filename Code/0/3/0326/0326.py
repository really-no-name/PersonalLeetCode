#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 3 的幂。
时间复杂度： O(1)
空间复杂度： O(1)
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            if 3 ** 19 % n == 0:
                return True
        return False
