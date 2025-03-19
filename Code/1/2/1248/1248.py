#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1248.py
作者: Bolun Xu
创建日期: 2025/3/19
版本: 1.0 -- 恰好型滑动窗口
描述: 统计「优美子数组」。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def subarraysOdd(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        odd_num = 0
        for right, num in enumerate(nums):
            if num % 2 != 0:
                odd_num += 1

            while odd_num > k:
                if nums[left] % 2 != 0:
                    odd_num -= 1
                left += 1

            ans += right - left + 1

        return ans

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        upper = self.subarraysOdd(nums, k)
        lower = self.subarraysOdd(nums, k - 1)
        return upper - lower


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
