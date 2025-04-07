#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1539.py
作者: Bolun Xu
创建日期: 2025/4/7
版本: 1.0
描述: 第 k 个缺失的正整数。
时间复杂度：
空间复杂度：
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = 1
        while True:
            if n not in (arr):
                k -= 1
            if k == 0:
                return n
            n += 1
