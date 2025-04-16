#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2185.py
作者: Bolun Xu
创建日期: 2025/4/16
版本: 1.0
描述: 统计包含给定前缀的字符串。
时间复杂度： O(N∗M)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        length = len(pref)
        cnt = 0
        for word in words:
            if word[:length] == pref:
                cnt += 1
        return cnt