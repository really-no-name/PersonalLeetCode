#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1544.py
作者: Bolun Xu
创建日期: 2025/4/8
版本: 1.0
描述: 整理字符串。
时间复杂度：
空间复杂度：
"""


class Solution:
    def check(self, s: str) -> bool:
        """
        检查是否字符串可被整理
        """
        for i in range(1, len(s)):
            if s[i].isupper() and s[i].lower() == s[i - 1]:
                return True
            elif s[i].islower() and s[i].upper() == s[i - 1]:
                return True
        return False

    def makeGood(self, s: str) -> str:
        if not self.check(s):
            return s
