#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1768.py
作者: Bolun Xu
创建日期: 2025/4/9
版本: 1.0
描述: 交替合并字符串。
时间复杂度： O(N)
空间复杂度： O(N)
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        ans = ''
        for i in range(n):
            ans += word1[i] + word2[i]
        if len(word1) < len(word2):
            ans += word2[n:]
        if len(word1) > len(word2):
            ans += word1[n:]
        return ans