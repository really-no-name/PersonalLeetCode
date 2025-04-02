#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1331.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 数组序号转换。
时间复杂度： O(Nlogn)
空间复杂度： O(N)
"""
import bisect
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sort = sorted(set(arr))
        # print(arr_sort)
        for i in range(len(arr)):
            arr[i] = bisect.bisect_right(arr_sort, arr[i])
        return arr


if __name__ == '__main__':
    sol = Solution()
    print(sol.arrayRankTransform([37,12,28,9,100,56,80,5,12]))