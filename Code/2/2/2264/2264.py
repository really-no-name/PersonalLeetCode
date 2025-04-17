#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2264.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 字符串中最大的 3 位相同数字。
时间复杂度： O(N)
空间复杂度： O(1)
"""
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                ans = max(ans, int(num[i]))
        if ans == -1:
            return ""
        else:
            return str(ans) * 3