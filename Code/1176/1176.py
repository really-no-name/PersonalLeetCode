#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1176.py
作者: Bolun Xu
创建日期: 2025/2/28
版本: 1.0
描述: 健身计划评估。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        ans = 0
        T = 0
        for i, c in enumerate(calories):
            T += c

            if i < k - 1:
                continue

            if T < lower:
                ans -= 1
            elif T > upper:
                ans += 1

            T -= calories[i - k + 1]
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.dietPlanPerformance(calories=[1, 2, 3, 4, 5], k=1, lower=3, upper=3))
