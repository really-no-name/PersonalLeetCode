#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0274.py
作者: Bolun Xu
创建日期: 2025/3/27
版本: 1.0
描述: H 指数。
时间复杂度： O(Nlogn)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        length = len(citations)
        left = 0
        right = length
        while left <= right:
            mid = (left + right) // 2
            if citations[-mid] >= mid:
                left = mid + 1
            else:
                right = mid - 1
        return right


if __name__ == '__main__':
    solution = Solution()
    print(solution.hIndex([3, 0, 6, 1, 5]))
