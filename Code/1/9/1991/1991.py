#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1991.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 1991。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1