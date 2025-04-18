#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2303.py
作者: Bolun Xu
创建日期: 2025/4/18
版本: 1.0
描述: 计算应缴税款总额。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0
        for i in range(len(brackets)):
            print(brackets[i])
            if income >= brackets[i][0]:
                if i != 0:
                    print('State 1', (brackets[i][0] - brackets[i - 1][0]) * brackets[i][1] / 100)
                    ans += (brackets[i][0] - brackets[i - 1][0]) * brackets[i][1] / 100
                else:
                    print('State 2', brackets[i][0] * brackets[i][1] / 100)
                    ans += brackets[i][0] * brackets[i][1] / 100
            else:
                if i != 0:
                    print('State 3', (income - brackets[i - 1][0]) * brackets[i][1] / 100)
                    ans += (income - brackets[i - 1][0]) * brackets[i][1] / 100
                else:
                    print('State 4', income * brackets[i][1] / 100)
                    ans += income * brackets[i][1] / 100
                break
        return ans