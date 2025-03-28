#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1618.py
作者: Bolun Xu
创建日期: 2025/3/28
版本: 1.0
描述: 找出适应屏幕的最大字号。
时间复杂度： O(N∗M)
空间复杂度： O(1)
"""
from typing import List


# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
class FontInfo(object):
   # Return the width of char ch when fontSize is used.
   def getWidth(self, fontSize, ch):
       """
       :type fontSize: int
       :type ch: char
       :rtype int
       """

   def getHeight(self, fontSize):
       """
       :type fontSize: int
       :rtype int
       """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo: 'FontInfo') -> int:
        left, right = 0, len(fonts) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            font_size = fonts[mid]

            # Check if font height is acceptable
            if fontInfo.getHeight(font_size) > h:
                right = mid - 1
                continue

            # Calculate total width
            total_width = sum(fontInfo.getWidth(font_size, char) for char in text)

            if total_width <= w:
                # This font size works, try larger ones
                result = font_size
                left = mid + 1
            else:
                # Font is too wide, try smaller ones
                right = mid - 1

        return result
