#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2716.py
作者: Bolun Xu
创建日期: 2025/3/28
版本: 1.0
描述: 最小化字符串长度。
时间复杂度：
空间复杂度：
"""


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))