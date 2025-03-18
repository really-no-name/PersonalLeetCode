#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode LCR_009.py
作者: Bolun Xu
创建日期: 2025/3/17
版本: 1.0
描述: 。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        left = 0
        window = 1
        for right, num in enumerate(nums):
            window *= num
            while window >= k:
                window //= nums[left]
                left += 1
            ans += right - left + 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
