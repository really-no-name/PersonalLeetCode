#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2894.py
作者: Bolun Xu
创建日期: 2025/5/27
版本: 1.0
描述: 分类求和并作差。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = num2 = 0
        for i in range(1, n + 1):
            print('DEBUG: ', i)
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1 - num2


if __name__ == '__main__':
    sol = Solution()
    print(sol.differenceOfSums(n=10, m=3))
