#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 完成旅途的最少时间 —— 二分写法。
时间复杂度： O(Log(Max(Time)*Totaltrips))
空间复杂度： O(1)
执行用时： 1188 ms
消耗内存： 29.94 mb
"""
import math
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 0
        right = max(time) * totalTrips + 1  # 最长时间为假设目标总趟数全部由蛋趟时间最长的车完成
        print(f"Debug: Initial bound: {left}, {right}")

        while left < right:
            mid = (left + right) // 2
            total = sum(mid // t for t in time)
            print(f"Debug: At time {mid}, total finish {total} trips")

            if total >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return right


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTime([1, 2, 3], 5))
    print(sol.minimumTime([5, 10, 10], 9))
