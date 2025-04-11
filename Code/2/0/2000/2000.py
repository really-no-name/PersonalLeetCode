#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2000.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 反转单词前缀。
时间复杂度： O(N)
空间复杂度： O(N)
"""
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s = list(word)
        try:
            idx = s.index(ch)
            print(s[:idx + 1])
            print(s[:idx + 1][::-1])
            return ''.join(s[:idx + 1][::-1] + s[idx + 1:])
        except ValueError:
            return word