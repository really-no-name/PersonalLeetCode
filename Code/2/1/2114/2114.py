#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2114.py
作者: Bolun Xu
创建日期: 2025/4/15
版本: 1.0
描述: 句子中的最多单词数。
时间复杂度： O(N∗M)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        cnt = 0
        for sentence in sentences:
            cnt = max(cnt, sentence.count(' '))
        return cnt + 1