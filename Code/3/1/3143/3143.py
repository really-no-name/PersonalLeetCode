#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3143.py
作者: Bolun Xu
创建日期: 2025/4/1
版本: 1.0
描述: 正方形中的最多点数。
时间复杂度： O(NLogM)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        res = 0

        def check(halfedge: int) -> bool:
            nonlocal res
            seen = {}
            for i in range(len(points)):
                if abs(points[i][0]) <= halfedge and abs(points[i][1]) <= halfedge:  # 在范围内
                    char = s[i]  # 对应标签
                    if char in seen:
                        return False
                    seen[char] = 1
            res = len(seen)
            return True

        left, right = -1, 10 ** 9 + 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxPointsInsideSquare(points=[[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], s="abdca"))
    print(s.maxPointsInsideSquare(points=[[1, 1], [-1, -1], [2, -2]], s="ccd"))
