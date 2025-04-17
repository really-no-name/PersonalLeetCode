#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2224.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 转化时间需要的最少操作数。
时间复杂度： O(1)
空间复杂度： O(1)
"""


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # 将时间转换为分钟数
        def time_to_minutes(time_str):
            hh, mm = map(int, time_str.split(':'))
            return hh * 60 + mm

        current_min = time_to_minutes(current)
        correct_min = time_to_minutes(correct)

        # 计算时间差，考虑跨过午夜的情况
        if correct_min >= current_min:
            diff = correct_min - current_min
        else:
            diff = (24 * 60 - current_min) + correct_min

        operations = 0
        # 贪心算法：尽可能先用大的时间增量
        for increment in [60, 15, 5, 1]:
            operations += diff // increment
            diff %= increment
            if diff == 0:
                break

        return operations
