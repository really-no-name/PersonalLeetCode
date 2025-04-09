#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1837.py
作者: Bolun Xu
创建日期: 2025/4/9
版本: 1.0
描述: K 进制表示下的各位数字总和。
时间复杂度： O(Logk∗Logn)
空间复杂度： O(Logk)
"""


class Solution:
    def decimal_to_k(self, n: int, k: int) -> int:
        """
        十进制 -> k 进制
        """
        if n == 0:
            return 0
        digits = []
        is_negative = n < 0
        n = abs(n)
        while n > 0:
            remainder = n % k
            # 处理 10-35 进制（用字母 A-Z 表示）
            if remainder >= 10:
                remainder = chr(ord('A') + remainder - 10)
            digits.append(str(remainder))
            n = n // k
        if is_negative:
            digits.append('-')
        return int(''.join(reversed(digits)))  # 逆序拼接

    def digit_sum(self, n: int) -> int:
        """
        数位和
        """
        n = abs(n)  # 处理负数
        total = 0
        while n > 0:
            total += n % 10  # 取最后一位
            n = n // 10  # 去掉最后一位
        return total

    def sumBase(self, n: int, k: int) -> int:
        n_k = self.decimal_to_k(n, k)
        ans = self.digit_sum(n_k)
        return ans
