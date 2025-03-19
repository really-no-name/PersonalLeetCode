#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2520.py
作者: Bolun Xu
创建日期: 2025/3/19
版本: 1.0
描述: 统计能整除数字的位数。
时间复杂度： O(N)
空间复杂度： O(N)
"""


class Solution:
    def countDigits(self, num: int) -> int:
        num_list = [int(digit) for digit in str(num)]
        ans = 0
        for n in num_list:
            if num % n == 0:
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countDigits(1248))