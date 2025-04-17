#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2210.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 统计数组中峰和谷的数量。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nums = [nums[i] for i in range(len(nums)) if i==0 or nums[i]!=nums[i-1]]
        print(nums)
        cnt = 0
        for i in range(1, len(nums) - 1):
            if (nums[i - 1] < nums[i] and nums[i] > nums[i + 1]) or (nums[i - 1] > nums[i] and nums[i] < nums[i + 1]):
                cnt += 1
        return cnt