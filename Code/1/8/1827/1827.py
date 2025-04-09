#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1827.py
作者: Bolun Xu
创建日期: 2025/4/9
版本: 1.0
描述: 最少操作使数组递增。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                cnt += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        return cnt