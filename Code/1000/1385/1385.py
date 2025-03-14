#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 两个数组间的距离值。
时间复杂度：O(NLogN+MLogM)
空间复杂度：O(1)
执行用时：7 ms
消耗内存：17.77 mb
"""
from bisect import bisect_left
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for x in arr1:
            left = x - d
            right = x + d
            pos = bisect_left(arr2, left)
            if pos < len(arr2) and arr2[pos] <= right:
                continue
            count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))
    print(sol.findTheDistanceValue(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3))
    print(sol.findTheDistanceValue(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6))
    print(sol.findTheDistanceValue(arr1=[-3, 2, -5, 7, 1], arr2=[4], d=84))
    print(sol.findTheDistanceValue(arr1=[-3, -3, 4, -1, -10], arr2=[7, 10], d=12))
