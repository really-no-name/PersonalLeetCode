#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 找到最高海拔。
时间复杂度： O(N)
空间复杂度： O(N)
执行用时：0 ms
消耗内存：17.37 mb
"""
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0] * (len(gain) + 1)
        for i in range(len(gain)):
            altitude[i + 1] = altitude[i] + gain[i]
        print(altitude)
        return max(altitude)


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestAltitude([-5, 1, 5, 0, -7]))
