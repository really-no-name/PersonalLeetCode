#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2351.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 第一个出现两次的字母。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import defaultdict


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        cnt = defaultdict(int)
        for char in s:
            cnt[char] += 1
            if cnt[char] == 2:
                return char
