#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1848.py
作者: Bolun Xu
创建日期: 2025/4/10
版本: 1.0
描述: 到目标元素的最小距离。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from math import inf
from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = inf
        for i, num in enumerate(nums):
            if num == target:
                ans = min(ans, abs(i - start))
        return ans