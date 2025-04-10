#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1876.py
作者: Bolun Xu
创建日期: 2025/4/10
版本: 1.0
描述: 长度为三且各字符不同的子字符串。
时间复杂度： O(N)
空间复杂度： O(1)
"""
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        s = list(s)
        cnt = 0
        for i in range(len(s) - 2):
            print(s[i: i + 3])
            if len(set(s[i: i + 3])) == 3:
                cnt += 1
        return cnt