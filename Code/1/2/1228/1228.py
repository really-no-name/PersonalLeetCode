#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1228.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 等差数列中缺失的数字。
时间复杂度：
空间复杂度：
"""
from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        tolerance = (arr[-1] - arr[0]) // len(arr)
        if tolerance == 0:
            return arr[0]

        # print(tolerance)
        for i in range(1, len(arr)):
            if arr[i] - arr[i -1] != tolerance:
                return arr[i - 1] + tolerance