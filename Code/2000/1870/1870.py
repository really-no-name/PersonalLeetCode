#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 准时到达的列车最小时速。
时间复杂度： O(Nlogn)
空间复杂度： O(1)
执行用时： 1283 ms
消耗内存： 28.22 mb
"""
import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1


        left = 0
        right = math.ceil(max(dist) / (len(dist) - 1))
        right = 10**9
        # print(f"Debug: Initial bound: {left}, {right}")

        while left < right:
            mid = (left + right) // 2
            time = sum(math.ceil(n / mid) for n in dist[:-1]) + dist[-1] / mid
            # print(f"Debug: if speed = {mid}, total need {time} hours")
            if time < hour:
                right = mid
            elif time > hour:
                left = mid + 1
            else:
                return mid

            # print(f"Debug: New bound {left}, {right}")
        return right


if __name__ == '__main__':
    sol = Solution()
    print("----------------Test 1 ------------------------")
    print(sol.minSpeedOnTime(dist=[1, 3, 2], hour=6))
    print("----------------Test 2 -----------------------")
    print(sol.minSpeedOnTime(dist=[1, 3, 2], hour=2.7))
    print("----------------Test 3 -----------------------")
    print(sol.minSpeedOnTime(dist=[1, 3, 2], hour=1.9))
