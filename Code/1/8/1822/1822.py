#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1822.py
作者: Bolun Xu
创建日期: 2025/4/9
版本: 1.0
描述: 数组元素积的符号。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        multiplication = 1
        for num in nums:
            multiplication *= num

        if multiplication > 0:
            return 1
        elif multiplication < 0:
            return -1
        else:
            return multiplication