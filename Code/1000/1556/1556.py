#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1556.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 千位分隔数。
时间复杂度： O(N)
空间复杂度： O(N)
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = ''
        for i, num in enumerate(str(n)[::-1]):
            if i % 3 == 0:
                ans += '.'
            ans += num
        return str(ans)[::-1][:-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.thousandSeparator(1000))