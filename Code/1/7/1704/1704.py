#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1704.py
作者: Bolun Xu
创建日期: 2025/4/8
版本: 1.0
描述: 判断字符串的两半是否相似。
时间复杂度： O(N)
空间复杂度： O(1)
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        split = 0.5 * len(s)
        print(split)
        left = 0
        right = 0
        for i in range(len(s)):
            print(s[i])
            if s[i] in 'aeiouAEIOU':
                if i >= split:
                    print("右加")
                    right += 1
                else:
                    print("左加")
                    left += 1
        return left == right
