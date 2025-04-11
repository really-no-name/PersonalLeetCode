#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1941.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 检查是否所有字符出现次数相同。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = Counter(s)
        return len(set(cnt.values())) <= 1
