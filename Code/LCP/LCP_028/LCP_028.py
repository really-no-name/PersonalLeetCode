#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode LCP_028.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 采购方案。
时间复杂度： O(Nlogn)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            s = nums[left] + nums[right]
            if s > target:
                right -= 1
            else:
                ans += right - left
                left += 1
        return ans % 1000000007


if __name__ == '__main__':
    sol = Solution()
    print(sol.purchasePlans(nums=[2, 5, 3, 5], target=6))
