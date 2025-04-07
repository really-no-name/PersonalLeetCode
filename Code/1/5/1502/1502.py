#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1502.py
作者: Bolun Xu
创建日期: 2025/4/7
版本: 1.0
描述: 判断能否形成等差数列。
时间复杂度： O(NLogN)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        # print(arr)
        tolerance = (arr[-1] - arr[0]) / (len(arr) - 1)
        # print(tolerance)
        if tolerance == 0:
            return True

        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1] + tolerance:
                return False
        return True