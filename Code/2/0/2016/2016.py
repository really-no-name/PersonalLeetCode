#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2016.py
作者: Bolun Xu
创建日期: 2025/4/13
版本: 1.0
描述: 增量元素之间的最大差值。
时间复杂度：
空间复杂度：
"""
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums) - 1):
            print(nums[i + 1:])
            m = max(nums[i + 1:])
            if m > nums[i]:
                ans = max(m - nums[i], ans)
        return ans