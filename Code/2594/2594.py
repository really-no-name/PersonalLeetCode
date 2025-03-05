#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2594.py
作者: Bolun Xu
创建日期: 2025/3/5
版本: 1.0
描述: 修车的最少时间。
时间复杂度： O(N*Log(M))
空间复杂度： O(1)
"""
from math import isqrt
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        :param ranks: 整数数组 ranks ，表示一些机械工的 能力值。ranks_i 是第 i 位机械工的能力值。
                        能力值为 r 的机械工可以在 r * n^2 分钟内修好 n 辆车。
        :param cars: 整数 cars ，表示总共需要修理的汽车数目。
        :return: 修理所有汽车 最少 需要多少时间。
        """

        def total_cars(t):
            s = 0
            for rank in ranks:
                s += isqrt(t // rank)
            return s

        left = 0
        right = cars ** 2 * max(ranks)
        while left < right:
            mid = (left + right) // 2
            if total_cars(mid) < cars:
                left = mid + 1
            else:
                right = mid
        return right


if __name__ == '__main__':
    sol = Solution()
    print(sol.repairCars(ranks=[4, 2, 3, 1], cars=10))
