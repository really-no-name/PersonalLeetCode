#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1891.py
作者: Bolun Xu
创建日期: 2025/3/28
版本: 1.0 -- 开区间二分
描述: 割绳子。
时间复杂度： O(NLogM)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if k > sum(ribbons):
            return 0
        elif k == sum(ribbons):
            return 1

        def check(x: int) -> bool:
            s = 0
            for ribbon in ribbons:
                s += ribbon // x
            return s >= k

        left = 0
        right = max(ribbons) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxLength(ribbons = [9,7,5], k = 3))