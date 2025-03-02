#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2958.py
作者: Bolun Xu
创建日期: 2025/3/2
版本: 1.0
描述: 最多 K 个重复元素的最长子数组。
时间复杂度： O(N)
空间复杂度： O(K)
"""
from collections import Counter
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        count = Counter()
        left = 0
        for right, num in enumerate(nums):
            count[num] += 1

            while count[num] > k:
                count[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))
    print(sol.maxSubarrayLength(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1))
