#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0171.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: Excel 表列序号。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        n = len(columnTitle) - 1
        for char in columnTitle:
            ans += (ord(char) - 65 + 1) * 26 ** n
            print(ans)
            n -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.titleToNumber('ZY'))
