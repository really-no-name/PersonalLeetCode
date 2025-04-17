#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0461.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 汉明距离。
时间复杂度： O(N)
空间复杂度： O(1)
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()