#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2309.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 兼具大小写的最好英文字母。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = ""
        for char in "ABCDEFGHIJKLMNOPQRSTYUVWXYZ":
            print(char)
            if char in s and char.lower() in s:
                ans = char
        return ans
