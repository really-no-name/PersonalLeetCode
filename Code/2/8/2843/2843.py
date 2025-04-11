#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2843.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 统计对称整数的数目。
时间复杂度： O(N∗M)
空间复杂度： O(1)
"""


class Solution:
    def is_symmetric_integer(self, x: int) -> bool:
        """
        检查一个由 2n 位数字组成的整数 x 是否为对称整数（前n位数字之和等于后n位数字之和）。
        如果 x 的位数不是偶数，直接返回 False。

        参数:
        x -- 要检查的整数

        返回:
        bool -- 如果是对称整数返回 True，否则返回 False
        """
        s = str(x)
        length = len(s)

        # 如果位数不是偶数，直接返回 False
        if length % 2 != 0:
            return False

        n = length // 2  # 计算前n位和后n位

        # 计算前n位数字之和
        first_half_sum = sum(int(digit) for digit in s[:n])

        # 计算后n位数字之和
        second_half_sum = sum(int(digit) for digit in s[n:])

        # 比较两部分的和是否相等
        return first_half_sum == second_half_sum

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for i in range(low, high + 1):
            if self.is_symmetric_integer(i):
                cnt += 1
        return cnt