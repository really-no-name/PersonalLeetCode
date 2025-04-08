#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1684.py
作者: Bolun Xu
创建日期: 2025/4/8
版本: 1.0
描述: 统计一致字符串的数目。
时间复杂度： O(N∗M)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        for word in words:
            if set(word) <= set(allowed):
                cnt += 1
        return cnt