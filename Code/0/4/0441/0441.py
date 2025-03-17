#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0441.py
作者: Bolun Xu
创建日期: 2025/3/17
版本: 1.0 -- 暴力求解
描述: 排列硬币。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        l = 2
        while True:
            total = (1 + l) * l * 0.5
            if total == n:
                return l
            elif total > n:
                return l - 1
            l += 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.arrangeCoins(4))
