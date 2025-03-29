#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1642.py
作者: Bolun Xu
创建日期: 2025/3/29
版本: 1.0
描述: 可以到达的最远建筑。
时间复杂度： O(NLogN)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diff = [0] * len(heights)
        for i in range(1, len(heights)):
            if heights[i] > heights[i - 1]:
                diff[i] = heights[i] - heights[i - 1]
        print(diff)

        def check(diff: List[int], k: int) -> int:
            if k - ladders <= 0:
                print(f"DEBUG: 需要 0 块砖")
                return 0

            if k > len(diff):
                k = len(diff)

                # 取前k个元素
            first_k = diff[:k]

            # 排序前k个元素
            sorted_first_k = sorted(first_k)

            # 取前(k - l)个最小的元素
            smallest_k_minus_l = sorted_first_k[:k - ladders]

            s= sum(smallest_k_minus_l)

            print(f"DEBUG: 需要 {s} 块砖")

            # 计算和
            return s

        left = 0
        right = len(heights) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            print(left, mid, right)
            if check(diff, mid) <= bricks:
                left = mid
            else:
                right = mid

        return left - 1


if __name__ == '__main__':
    s = Solution()
    print(s.furthestBuilding(heights=[1, 13, 1, 1, 13, 5, 11, 11], bricks=10, ladders=8))
    print(s.furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))
