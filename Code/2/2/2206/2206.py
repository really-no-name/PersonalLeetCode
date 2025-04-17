#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2206.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 将数组划分成相等数对。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for key in cnt.keys():
            if cnt[key] % 2 != 0:
                return False
        return True