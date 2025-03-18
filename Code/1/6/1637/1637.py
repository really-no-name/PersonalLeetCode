#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1637.py
作者: Bolun Xu
创建日期: 2025/3/18
版本: 1.0
描述: 两点之间不包含任何点的最宽垂直区域。
时间复杂度： O(Nlogn)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_list = []
        for value in points:
            x_list.append(value[0])
        x_list.sort()
        ans = 0
        for i in range(1, len(x_list) - 1):
            ans = max(x_list[i] - x_list[i - 1], ans)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]))
    print(solution.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
