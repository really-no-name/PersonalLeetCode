#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1750.py
作者: Bolun Xu
创建日期: 2025/3/19
版本: 1.0
描述: 删除字符串两端相同字符后的最短长度。
时间复杂度：
空间复杂度：
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:  # 删除前缀
                left += 1
            while left <= right and s[right] == char:  # 删除后缀
                right -= 1
        return right - left + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumLength('abc'))
