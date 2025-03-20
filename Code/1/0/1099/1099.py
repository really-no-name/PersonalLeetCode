#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1099.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 小于 K 的两数之和。
时间复杂度：
空间复杂度：
"""
from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        ans = -1

        while left < right:
            if nums[left] + nums[right] >= k:
                right -= 1
            else:
                ans = max(ans, nums[left] + nums[right])
                left += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSumLessThanK(nums=[34, 23, 1, 24, 75, 33, 54, 8], k=60))
