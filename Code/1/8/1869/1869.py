#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1869.py
作者: Bolun Xu
创建日期: 2025/4/10
版本: 1.0
描述: 哪种连续子字符串更长。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        def check(s: List[str]) -> int:
            m = 0
            for char in s:
                m = max(m, len(char))
            return m

        split_0 = s.split('0')
        split_1 = s.split('1')
        return check(split_0) > check(split_1)