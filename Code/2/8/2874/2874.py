#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2874.py
作者: Bolun Xu
创建日期: 2025/4/3
版本: 1.0
描述: 有序三元组中的最大值 II。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suf_max = [0] * (n + 1)
        for i in range(n - 1, 1, -1):
            suf_max[i] = max(suf_max[i + 1], nums[i])

        ans = pre_max = 0
        for j, x in enumerate(nums):
            ans = max(ans, (pre_max - x) * suf_max[j + 1])
            pre_max = max(pre_max, x)
        return ans
