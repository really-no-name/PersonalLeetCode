#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0875.py
作者: Bolun Xu
创建日期: 2025/3/4
版本: 1.0
描述: 爱吃香蕉的珂珂。
时间复杂度： O(N∗Max(Piles))
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        print(f"DEBUG: 初始边界为 {left}, {right}")
        while left + 1 < right:
            mid = (left + right) // 2
            print(f"DEBUG: 中间值为 {mid}, 边界为 {left}, {right}")
            total_time = sum((p - 1) // mid for p in piles)
            print(f"DEBUG: 当前需要的时间为 {total_time}")
            if total_time <= h - len(piles):
                right = mid
            else:
                left = mid
        return right


if __name__ == '__main__':
    sol = Solution()
    print(sol.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
