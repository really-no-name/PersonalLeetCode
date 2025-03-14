#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1482.py
作者: Bolun Xu
创建日期: 2025/3/5
版本: 1.0
描述: 制作 m 束花所需的最少天数。
时间复杂度： O(Nlog(N))
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        :param bloomDay: 第 i 朵花会在 bloomDay[i] 时盛开
        :param m: 需要的花束
        :param k: 每束花需要的花数量
        :return:
        """
        if len(bloomDay) < m * k:
            return -1

        left = min(bloomDay)
        right = max(bloomDay)
        # print(f"DEBUG: 初始边界 {left}, {right}")
        while left < right:
            mid = (left + right) // 2
            # print(f"DEBUG: mid = {mid}, left = {left}, right = {right}")
            # print(f"DEBUG: 当前可制作 {self.count_consecutive_ones(bloomDay, k, mid)}")
            if self.count_consecutive_ones(bloomDay, k, mid) < m:
                left = mid + 1
            else:
                right = mid
        return right

    def count_consecutive_ones(self, bloomDay: List[int], k: int, day: int) -> int:
        """
        :param bloomDay:
        :param k: 每束花需要的花数量
        :param day:
        :return: 在 day 天可制作的花束
        """
        binary_list = []
        for blo in bloomDay:
            if blo <= day:
                binary_list.append(1)
            else:
                binary_list.append(0)
        # print(f"DEBUG: 当前开放情况为 {binary_list}")
        count = 0
        consecutive = 0

        for num in binary_list:
            if num == 1:
                consecutive += 1
            else:
                consecutive = 0

            if consecutive == k:
                count += 1
                consecutive = 0  # 重置计数，避免重叠

        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))
    print(sol.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2))
    print(sol.minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3))
