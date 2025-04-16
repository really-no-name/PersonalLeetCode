#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2229.py
作者: Bolun Xu
创建日期: 2025/4/16
版本: 1.0
描述: 检查数组是否连贯。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return False
        low = min(nums)
        up = max(nums)
        return up - low + 1 == len(nums)