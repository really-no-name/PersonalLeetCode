#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2341.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 数组能形成多少数对。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        count = 0
        left = 0
        for key in cnt.keys():
            count += cnt[key] // 2
            left += cnt[key] % 2
        return [count, left]