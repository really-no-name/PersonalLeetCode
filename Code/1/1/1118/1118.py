#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1118.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 一月有多少天。
时间复杂度： O(1)
空间复杂度： O(1)
"""
import calendar


class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        return calendar.monthrange(year, month)[1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfDays(2020, 1))
