#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0264.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
class Solution:
    def isUgly(self, n: int) -> bool:
        if n > 0:
            while n % 5 == 0:
                n //= 5
            while n % 3 == 0:
                n //= 3
            if n & (n - 1) == 0:
                return True
        return False

    def nthUglyNumber(self, n: int) -> int:
        k = 1

        return k


if __name__ == '__main__':
    sol = Solution()
    print(sol.nthUglyNumber(10))