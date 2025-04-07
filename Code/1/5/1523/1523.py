#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1523.py
作者: Bolun Xu
创建日期: 2025/4/7
版本: 1.0
描述: 在区间范围内统计奇数数目。
时间复杂度： O(1)
空间复杂度： O(1)
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1
        return (high - low) // 2 + 1