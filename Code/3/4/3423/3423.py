#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3423.py
作者: Bolun Xu
创建日期: 2025/6/12
版本: 1.0
描述: 循环数组中相邻元素的最大差值。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        for i in range(len(nums)):
            print('DEBUG', nums[i])
            if i == len(nums):
                max_diff = max(max_diff, abs(nums[0] - nums[i]))
            else:
                max_diff = max(max_diff, abs(nums[i] - nums[i - 1]))
        return max_diff


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxAdjacentDistance([1, 2, 4]))