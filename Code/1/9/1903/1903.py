#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1903.py
作者: Bolun Xu
创建日期: 2025/4/10
版本: 1.0
描述: 字符串中的最大奇数。
时间复杂度： O(N)
空间复杂度： O(1)
"""
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            print(num[i])
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""