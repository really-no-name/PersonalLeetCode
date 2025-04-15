#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2124.py
作者: Bolun Xu
创建日期: 2025/4/15
版本: 1.0
描述: 检查是否所有 A 都在 B 之前。
时间复杂度： O(N)
空间复杂度： O(1)
"""
class Solution:
    def checkString(self, s: str) -> bool:
        if 'b' not in s:
            return True
        idx = s.find('b')
        print(idx, s[idx])
        for i in range(idx, len(s)):
            if s[i] == 'a':
                return False
        return True