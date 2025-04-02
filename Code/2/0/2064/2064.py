#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2064.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 分配给商店的最多商品的最小值。
时间复杂度： O(N∗Log(Sum(Quantities)))
空间复杂度： O(1)
"""
import math
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(m: int) -> bool:
            shop = 0
            for quantity in quantities:
                shop += math.ceil(quantity / m)
            print(f"DEBUG: 当前可分给 {shop} 个商店")
            if shop > n:
                return False
            else:
                return True

        left = 0
        right = sum(quantities) + 1
        while left + 1 < right:
            mid = (right + left) // 2
            print(f"DEBUG: {left}, {mid}, {right}")
            if check(mid):
                right = mid
            else:
                left = mid
        return right


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimizedMaximum(n = 6, quantities = [11,6]))