#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1961.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 检查字符串是否为数组前缀。
时间复杂度： O(N∗M)
空间复杂度： O(M)
"""
from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        s_new = ''
        for word in words:
            s_new += word
            if s_new == s:
                return True
        return False