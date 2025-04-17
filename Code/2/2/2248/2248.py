#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2248.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 多个数组求交集。
时间复杂度： O（N^2LogN)
空间复杂度： O(N)
"""
from functools import reduce
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if not nums:
            return []

        # 使用reduce连续求交集
        return sorted(reduce(lambda x, y: set(x) & set(y), nums))