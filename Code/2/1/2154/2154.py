#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2154.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 将找到的值乘以 2。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while True:
            if original in nums:
                original *= 2
            else:
                break
        return original