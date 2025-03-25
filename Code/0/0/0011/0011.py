#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0011.py
作者: Bolun Xu
创建日期: 2025/3/25
版本: 2.0
描述: 盛最多水的容器。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                max_area = max(area, max_area)
                left += 1
            else:
                area = height[right] * (right - left)
                max_area = max(area, max_area)
                right -= 1
        return max_area


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
