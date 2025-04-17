#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2239.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 找到最接近 0 的数字。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for num in nums:
            if (abs(num) < abs(ans)
                or abs(num) == abs(ans)
                and num > 0):
                ans = num
        return ans