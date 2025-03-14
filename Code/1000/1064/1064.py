#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 不动点。
时间复杂度： O(NLogN)
空间复杂度： O(LogN)
执行用时： 0 ms
消耗内存： 18.31 mb
"""
from bisect import bisect_left
from typing import List


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i] == bisect_left(arr, i):
                return i
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.fixedPoint(arr=[-10, -5, 0, 3, 7]))
