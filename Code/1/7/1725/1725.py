#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1725.py
作者: Bolun Xu
创建日期: 2025/4/8
版本: 1.0
描述: 可以形成最大正方形的矩形数目。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        for rectangle in rectangles:
            maxLen = max(maxLen, min(rectangle[0], rectangle[1]))
        # print(maxLen)
        cnt = 0
        for rectangle in rectangles:
            if min(rectangle[0], rectangle[1]) >= maxLen:
                cnt += 1
        return cnt