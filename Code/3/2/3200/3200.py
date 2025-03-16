#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3200.py
作者: Bolun Xu
创建日期: 2025/3/16
版本: 1.0
描述: 三角形的最大高度。
时间复杂度： O(1)
空间复杂度： O(1)
"""
import math


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # 解二次方程 n^2 + n - 2k = 0
        discriminant = 1 + 8 * (red + blue)
        l = (-1 + math.sqrt(discriminant)) / 2
        m = int(l) // 2 + 2  # 偶数行数
        n = m + 1
        while True:
            # 奇数行球数
            odd = n ** 2
            even = m ** 2 + m
            print(f"DEBUG: n = {n}, m = {m} 时， odd = {odd}, even = {even}")
            if odd <= red and even <= blue:
                print(f"DEBUG: 红色放奇数行，使用 {odd} 个， 蓝色使用 {even} 个")
                return m + n
            elif odd <= blue and even <= red:
                print(f"DEBUG: 红色放偶数行，使用 {even} 个， 蓝色使用 {odd} 个")
                return m + n

            if (m + n) % 2 == 0:
                m -= 1
            else:
                n -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.maxHeightOfTriangle(red=5, blue=7))
    print(s.maxHeightOfTriangle(red=45, blue=26))
