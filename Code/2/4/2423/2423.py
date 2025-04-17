#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2423.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0 -- 暴力求解
描述: 删除字符使频率相同。
时间复杂度： O(N^2)
空间复杂度： O(N)
"""
from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):  # 枚举删除的字符
            cnt = Counter(word[:i] + word[i + 1:])  # 统计出现次数
            if len(set(cnt.values())) == 1:  # 出现次数都一样
                return True
        return False