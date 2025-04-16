#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2176.py
作者: Bolun Xu
创建日期: 2025/4/16
版本: 1.0
描述: 统计数组中相等且可以被整除的数对。
时间复杂度： O(N^2)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    cnt += 1
        return cnt