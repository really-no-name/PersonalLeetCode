#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1979.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 找出数组的最大公约数。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        for i in range(max_num, 0, -1):
            if int(max_num / i) == max_num / i and int(min_num / i) == min_num / i:
                return i