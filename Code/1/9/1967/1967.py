#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1967.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 作为子字符串出现在单词中的字符串数目。
时间复杂度： O(M∗N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0
        for pattern in patterns:
            if pattern in word:
                cnt += 1
        return cnt