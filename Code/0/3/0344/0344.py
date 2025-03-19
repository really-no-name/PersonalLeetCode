#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0344.py
作者: Bolun Xu
创建日期: 2025/3/19
版本: 1.0
描述: 反转字符串。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        char = ''
        while left < right:
            char = s[left]
            s[left] = s[right]
            s[right] = char

            left += 1
            right -= 1


if __name__ == '__main__':
    solution = Solution()
    s = ["h", "e", "l", "l", "o"]
    solution.reverseString(s)
    print(s)
