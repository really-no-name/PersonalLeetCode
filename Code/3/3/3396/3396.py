#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3396.py
作者: Bolun Xu
创建日期: 2025/4/9
版本: 1.0
描述: 使数组元素互不相同所需的最少操作次数。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        k = 0
        while True:
            if len(nums) == len(set(nums)):
                return k
            elif len(nums) > len(set(nums)):
                if len(nums) > 3:
                    nums = nums[3:]
                    k += 1
                elif len(nums) <= 3:
                    k += 1
                    return k