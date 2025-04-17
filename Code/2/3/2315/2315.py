#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2315.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 统计星号。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        state = 1
        cnt = 0
        for char in s:
            print(char, state)
            if char == '|':
                if state == 0:
                    state = 1
                elif state == 1:
                    state = 0
            if char == '*':
                cnt += state
        return cnt
