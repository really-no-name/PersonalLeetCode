#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1897.py
作者: Bolun Xu
创建日期: 2025/4/10
版本: 1.0
描述: 重新分配字符使所有字符串都相等。
时间复杂度： O(N∗K)
空间复杂度： O(K)
"""
from collections import Counter
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        length = len(words)
        cnt = Counter()
        for word in words:
            cnt += Counter(word)
            print(cnt)
        for key in cnt.keys():
            if (cnt[key] / length) % 1 != 0:
                return False
        return True