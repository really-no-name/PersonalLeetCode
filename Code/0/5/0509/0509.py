#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0509.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 斐波那契数。
时间复杂度： O(1)
空间复杂度： O(1)
"""
from math import sqrt


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return int((((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) / sqrt(5))