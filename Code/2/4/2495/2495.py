#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2495.py
作者: Bolun Xu
创建日期: 2025/3/17
版本: 1.0
描述: 乘积为偶数的子数组数。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        window = 1
        for right, num in enumerate(nums):
            window *= num
            while window % 2 == 0:
                window //= nums[left]  # ? 整除
                left += 1
            ans += left
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.evenProduct([9, 6, 7, 13]))
