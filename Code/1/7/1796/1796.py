#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1796.py
作者: Bolun Xu
创建日期: 2025/4/9
版本: 1.0
描述: 字符串中第二大的数字。
时间复杂度： O(NLogN)
空间复杂度： O(N)
"""
class Solution:
    def secondHighest(self, s: str) -> int:
        num = []
        for char in s:
            try:
                num.append(int(char))
            except ValueError:
                continue
        num = sorted(set(num))
        return num[-2] if len(num) >= 2 else -1