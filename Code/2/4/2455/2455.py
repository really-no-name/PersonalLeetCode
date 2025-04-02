#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2455.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 可被三整除的偶数的平均值。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        n = 0
        s = 0
        for num in nums:
            if num % 3 == 0 and num % 2 == 0:
                n += 1
                s += num
        if n == 0:
            return 0
        return s // n