#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2799.py
作者: Bolun Xu
创建日期: 2025/3/17
版本: 1.0
描述: 统计完全子数组的数目。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import defaultdict
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        length = len(set(nums))
        cnt = defaultdict(int)
        left = 0
        ans = 0
        for num in nums:
            cnt[num] += 1
            while len(cnt) == length:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ans += left
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countCompleteSubarrays([1, 3, 1, 2, 2]))
