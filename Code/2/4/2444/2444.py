#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2444.py
作者: Bolun Xu
创建日期: 2025/4/26
版本: 1.0
描述: 统计定界子数组的数目。
时间复杂度：
空间复杂度：
"""
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_i = max_i = i0 = -1
        for i, x in enumerate(nums):
            if x == minK:
                min_i = i  # 最近的 minK 位置
            if x == maxK:
                max_i = i  # 最近的 maxK 位置
            if not minK <= x <= maxK:
                i0 = i  # 子数组不能包含 nums[i0]
            ans += max(min(min_i, max_i) - i0, 0)
        return ans
