#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1154.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 一年中的第几天。
时间复杂度： O(1)
空间复杂度： O(1)
"""


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # 判断闰年
        def is_leap_year(y):
            return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

        day_of_year = 0
        for m in range(month - 1):
            day_of_year += days_in_month[m]

        day_of_year += day

        if month > 2 and is_leap_year(year):
            day_of_year += 1

        return day_of_year