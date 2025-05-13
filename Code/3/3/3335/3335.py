#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3335.py
作者: Bolun Xu
创建日期: 2025/5/13
版本: 1.0 -- ？
描述: 字符串转换后的长度 I。
时间复杂度：
空间复杂度：
"""

MOD = 10 ** 9 + 7


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(c, k):
            if k == 0:
                return 1
            if c != 'z':
                next_char = chr(ord(c) + 1)
                return dp(next_char, k - 1)
            else:
                return (dp('a', k - 1) + dp('b', k - 1)) % MOD

        total = 0
        for char in s:
            total = (total + dp(char, t)) % MOD
        return total


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthAfterTransformations('abcyy', 2))
