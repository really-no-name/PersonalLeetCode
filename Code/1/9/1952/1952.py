#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1952.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 三除数。
时间复杂度： O(N)
空间复杂度： O(1)
"""
class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 0
        for i in range(1, n + 1):
            print(i)
            if int(n / i) == n / i:
                cnt += 1
        return cnt == 3