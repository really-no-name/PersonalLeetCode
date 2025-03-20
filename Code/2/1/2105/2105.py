#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2105.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 给植物浇水 II。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        left = 0
        right = len(plants) - 1
        a = capacityA
        b = capacityB
        ans = 0
        while left < right:
            if a < plants[left]:
                ans += 1
                a = capacityA
            a -= plants[left]
            left += 1

            if b < plants[right]:
                ans += 1
                b = capacityB
            b -= plants[right]
            right -= 1

        # Alice 和 Bob 到达同一株植物，那么当前水罐中水更多的人会给这株植物浇水
        if left == right and max(a, b) < plants[left]:
            ans += 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumRefill(plants=[2, 2, 3, 3], capacityA=5, capacityB=5))
