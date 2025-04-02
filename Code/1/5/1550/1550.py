#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1550.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 存在连续三个奇数的数组。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False
