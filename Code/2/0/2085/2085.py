#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2085.py
作者: Bolun Xu
创建日期: 2025/4/14
版本: 1.0
描述: 统计出现过一次的公共字符串。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)
        cnt = 0
        for key in cnt1.keys():
            if cnt1[key] == 1 and cnt2[key] == 1:
                cnt += 1
        return cnt