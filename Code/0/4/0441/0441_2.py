#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0441.py
作者: Bolun Xu
创建日期: 2025/3/17
版本: 2.0 -- 数学
描述: 排列硬币。
时间复杂度： O(1)
空间复杂度： O(1)
"""
import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 解二次方程 l^2 + l - 2n = 0
        discriminant = 1 + 8 * n
        l = (-1 + math.sqrt(discriminant)) / 2
        return int(l)


if __name__ == '__main__':
    sol = Solution()
    print(sol.arrangeCoins(4))
