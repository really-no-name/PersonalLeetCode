#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 有序数组中出现次数超过25%的元素 —— 暴力循环。
时间复杂度：O(NLogN)
空间复杂度：O(LogN)
执行用时：0 ms
消耗内存：18.41 mb
"""
import bisect
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            left = i
            right = bisect.bisect_right(arr, arr[i])
            length = right - left
            # print(arr[i], left, right, "length", length)
            if length > 0.25 * len(arr):
                return arr[i]


if __name__ == '__main__':
    s = Solution()
    print(s.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
