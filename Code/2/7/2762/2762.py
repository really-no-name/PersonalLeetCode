#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2762.py
作者: Bolun Xu
创建日期: 2025/3/18
版本: 1.0
描述: 不间断子数组。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        cnt = Counter()
        left = 0
        ans = 0
        for right, num in enumerate(nums):
            cnt[num] += 1

            while max(cnt) - min(cnt) > 2:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1

            ans += right - left + 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.continuousSubarrays([5, 4, 2, 4]))
