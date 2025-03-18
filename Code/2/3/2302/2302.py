#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2302.py
作者: Bolun Xu
创建日期: 2025/3/18
版本: 1.0
描述: 统计得分小于 K 的子数组数目。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        window_sum = 0
        left = 0
        ans = 0
        for right, num in enumerate(nums):
            window_sum += num

            while window_sum * (right - left + 1) >= k:
                window_sum -= nums[left]
                left += 1

            ans += right - left + 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubarrays(nums=[2, 1, 4, 3, 5], k=10))
