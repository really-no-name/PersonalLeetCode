#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0101.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 判断偶数。
"""

import sys
import os
import re

class Solution:
    def isEvenNum(self, n):
        if n % 2 == 0:
            return 1
        else:
            return 0

n = int(input())


s = Solution()
res = s.isEvenNum(n)

print(res)