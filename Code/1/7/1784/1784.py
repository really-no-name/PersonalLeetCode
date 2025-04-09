#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1784.py
作者: Bolun Xu
创建日期: 2025/4/9
版本: 1.0
描述: 检查二进制字符串字段。
时间复杂度： O(N)
空间复杂度： O(1)
"""
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s