#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1493.py
作者: Bolun Xu
创建日期: 2025/3/2
版本: 1.0
描述: 删掉一个元素以后全为 1 的最长子数组。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        for right, num in enumerate(nums):
            cnt[num] += 1
            # print(cnt)
            while cnt[0] > 1:
                cnt[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        return ans - 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubarray([1, 1, 0, 1]))
