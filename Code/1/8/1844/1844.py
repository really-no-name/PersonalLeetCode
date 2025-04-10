#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1844.py
作者: Bolun Xu
创建日期: 2025/4/9
版本: 1.0
描述: 将所有数字用字符替换。
时间复杂度： O(N)
空间复杂度： O(N)
"""


class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c: str, x: int) -> str:
            return chr(ord(c) + x)

        ans = []
        for i in range(0, len(s), 2):
            ans.append(s[i])
            if i + 1 < len(s):
                ans.append(shift(s[i], int(s[i + 1])))

        return ''.join(ans)