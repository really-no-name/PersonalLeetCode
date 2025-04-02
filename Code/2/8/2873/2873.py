#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2873.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 有序三元组中的最大值 I。
时间复杂度： O(N^3)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            for j in range(i+ 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])
        return ans