#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2027.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 转换字符串的最少操作次数。
时间复杂度： O(N)
空间复杂度： O(1)
"""
class Solution:
    def minimumMoves(self, s: str) -> int:
        cnt = 0
        i = 0
        while i < len(s):
            if s[i] == 'X':
                cnt += 1
                i += 3
            else:
                i += 1
        return cnt