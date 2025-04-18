#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2200.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 找出数组中的所有 K 近邻下标。
时间复杂度： O(N^2)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_idx = [i for i, num in enumerate(nums) if num == key]
        print(key_idx)
        ans = []
        for i in range(len(nums)):
            if i in key_idx:
                ans.append(i)
                continue

            for idx in key_idx:
                if abs(i - idx) <= k:
                    ans.append(i)
                    continue
        return sorted(set(ans))