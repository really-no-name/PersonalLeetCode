#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2875.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 无限数组的最短子数组。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from math import inf
from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)
        nums_n = nums + nums
        target_n = target % total
        ans = inf
        left = s = 0
        for right, num in enumerate(nums_n):
            s += num
            while s > target_n:
                s -= nums_n[left]
                left += 1
            if s == target_n:
                ans = min(ans, right - left + 1)
        if ans < inf:
            return ans + target // total * n
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSizeSubarray(nums=[2, 4, 6, 8], target=3))
    print(sol.minSizeSubarray(nums=[1, 1, 1, 2, 3], target=4))
