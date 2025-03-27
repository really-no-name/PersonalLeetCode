#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2982.py
作者: Bolun Xu
创建日期: 2025/3/27
版本: 1.0
描述: 找出出现至少三次的最长特殊子字符串 II。
时间复杂度：
空间复杂度：
"""


class Solution:
    def maximumLength(self, s: str) -> int:
        left = 0
        right = len(s)
        while left + 1 < right:
            mid = (left + right) // 2
        return left


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumLength("aaaa"))
