#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1748.py
作者: Bolun Xu
创建日期: 2025/4/8
版本: 1.0
描述: 唯一元素的和。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for k in cnt.keys():
            if cnt[k] == 1:
                ans += k
        return ans