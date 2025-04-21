#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 17_21.py
作者: Bolun Xu
创建日期: 2025/3/26
版本: 1.0
描述: 直方图的水量。
时间复杂度：
空间复杂度：
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = right_max = 0
        ans = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans