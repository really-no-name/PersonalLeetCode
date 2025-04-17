#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2220.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 转换数字的最少位翻转次数。
时间复杂度： O(Logn)
空间复杂度： O(1)
"""
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        异或运算 (^) 的规则是：如果两个比特不同，则结果为 1，否则为 0
        Python 3.10+ 提供了 int.bit_count() 方法，用于计算整数的二进制表示中 1 的个数。
        """
        ans = start ^ goal
        print(bin(ans))
        return ans.bit_count()