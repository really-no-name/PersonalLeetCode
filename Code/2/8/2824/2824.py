#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2824.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 统计和小于目标的下标对数目。
时间复杂度： O(Nlogn)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(f"DEBUG: nums={nums}")
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            if nums[left] + nums[right] >= target:
                right -= 1
            else:
                print(f"DEBUG: {nums[left]}, {nums[right]} 满足要求")
                ans += right - left
                left += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPairs(nums=[-1, 1, 2, 3, 1], target=2))
