#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1708.py
作者: Bolun Xu
创建日期: 2025/4/8
版本: 1.0
描述: 长度为 K 的最大子数组。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        print(F"DEBUG: {nums[:-(k - 1)]}")
        max_num = max(nums[:-(k - 1)]) if k > 1 else max(nums)
        return nums[nums.index(max_num):nums.index(max_num)+k]
