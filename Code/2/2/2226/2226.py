#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2226.py
作者: Bolun Xu
创建日期: 2025/3/27
版本: 1.0 -- 开区间二分答案
描述: 每个小孩最多能分到多少糖果。
时间复杂度： O(NLogM)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k > sum(candies):
            return 0
        elif k == sum(candies):
            return 1

        def check(c: int) -> bool:
            s = 0
            for candie in candies:
                s += candie // c
            return s >= k

        left = 0
        right = max(candies) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            print(f"{left}, {mid}, {right}")
            if check(mid):
                left = mid
            else:
                right = mid

        return left


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumCandies(candies = [5,8,6], k = 3))
    print(sol.maximumCandies(candies = [3102006,6279432,7216621,3628028,5711306,2292506,2107393], k = 23626985))