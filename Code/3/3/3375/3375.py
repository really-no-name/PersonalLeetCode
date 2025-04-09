#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3375.py
作者: Bolun Xu
创建日期: 2025/4/9
版本: 1.0
描述: 使数组的值全部为 K 的最少操作次数。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        if k in set(nums):
            return len(set(nums)) - 1
        elif k not in set(nums):
            return len(set(nums))