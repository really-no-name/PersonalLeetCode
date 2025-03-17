#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0029.py
作者: Bolun Xu
创建日期: 2025/3/17
版本: 1.0
描述: 两数相除。
时间复杂度： O(Logn)
空间复杂度： O(1)
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 处理溢出情况
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        # 特殊情况：被除数为最小值，除数为-1，结果会溢出
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # 确定结果的符号
        negative = (dividend < 0) ^ (divisor < 0)

        # 将被除数和除数转换为正数
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # 使用位运算和减法模拟除法
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple

        # 根据符号返回结果
        if negative:
            quotient = -quotient

        # 处理溢出
        if quotient < INT_MIN:
            return INT_MIN
        elif quotient > INT_MAX:
            return INT_MAX
        else:
            return quotient


if __name__ == '__main__':
    sol = Solution()
    print(sol.divide(10, 3))
    print(sol.divide(-2147483648, -1))
    print(2 ** 31)
