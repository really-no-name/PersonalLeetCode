#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1805.py
作者: Bolun Xu
创建日期: 2025/4/9
版本: 1.0
描述: 字符串中不同整数的数目。
时间复杂度： O(N)
空间复杂度： O(N)
"""
import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        """
        提取连续数字
        """
        numbers = list(map(int, re.findall(r'\d+', word)))
        # re.findall(r'\d+', s)：提取所有连续的数字（如 '123', '34', '8', '34'）。
        # map(int, ...)：将每个字符串数字转换为整数（如 '123' → 123）。
        # list(...)：将 map 对象转换为 List[int]。
        return len(set(numbers))


