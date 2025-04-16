#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2537.py
作者: Bolun Xu
创建日期: 2025/4/16
版本: 1.0
描述: 统计好子数组的数目。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import defaultdict
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        left = 0
        ans = 0
        pairs = 0
        for right in nums:
            pairs += cnt[right]
            cnt[right] += 1
            while pairs >= k:
                cnt[nums[left]] -= 1
                pairs -= cnt[nums[left]]
                left += 1
            ans += left
        return ans