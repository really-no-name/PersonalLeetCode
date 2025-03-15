#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3110.py
作者: Bolun Xu
创建日期: 2025/3/15
版本: 1.0
描述: 字符串的分数。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def scoreOfString(self, s: str) -> int:
        left = 0
        right = ord(s[0])
        ans = 0
        for i in range(len(s) - 1):
            left = right
            right = ord(s[i + 1])
            ans += abs(right - left)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.scoreOfString("hello"))