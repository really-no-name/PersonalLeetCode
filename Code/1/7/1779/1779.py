#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1779.py
作者: Bolun Xu
创建日期: 2025/4/9
版本: 1.0
描述: 找到最近的有相同 X 或 Y 坐标的点。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from math import inf
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_manhattan = inf
        min_manhattan_idx = -1
        for i, point in enumerate(points):
            if point[0] != x and point[1] != y:
                continue
            else:
                manhattan = abs(point[0] - x) + abs(point[1] - y)
                if manhattan < min_manhattan:
                    min_manhattan = manhattan
                    min_manhattan_idx = i
        return min_manhattan_idx