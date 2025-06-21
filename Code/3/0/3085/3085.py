#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3085.py
作者: Bolun Xu
创建日期: 2025/6/21
版本: 1.0
描述: 成为 K 特殊字符串需要删除的最少字符数。
时间复杂度：
空间复杂度：
"""
from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = sorted(Counter(word).values())
        max_save = 0
        for i, base in enumerate(cnt):
            s = sum(min(c, base + k) for c in cnt[i:])  # 至多保留 base+k 个
            max_save = max(max_save, s)
        return len(word) - max_save
