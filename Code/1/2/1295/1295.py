#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1295.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 统计位数为偶数的数字。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ans += 1
        return ans