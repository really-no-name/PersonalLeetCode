#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 山脉数组的峰顶索引 —— 开区间二分。
时间复杂度：
空间复杂度：
执行用时：
消耗内存：
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:  # 增长
                right = mid
            else:
                left = mid + 1
        return right


if __name__ == '__main__':
    sol = Solution()
    print(sol.peakIndexInMountainArray([0, 2, 1, 0]))
