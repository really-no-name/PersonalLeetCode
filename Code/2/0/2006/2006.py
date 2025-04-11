#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2006.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 差的绝对值为 K 的数对数目。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        nums = set(nums)
        ans = 0
        for num in nums:
            print('num', num)
            if k + num in nums:
                print(k + num)
                ans += cnt[k + num] * cnt[num]
        return ans