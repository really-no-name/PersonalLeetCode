#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2068.py
作者: Bolun Xu
创建日期: 2025/4/14
版本: 1.0
描述: 检查两个字符串是否几乎相等。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        for key in cnt1.keys():
            if abs(cnt1[key] - cnt2[key]) > 3:
                return False

        for key in cnt2.keys():
            if abs(cnt1[key] - cnt2[key]) > 3:
                return False

        return True