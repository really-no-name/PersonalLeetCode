#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2278.py
作者: Bolun Xu
创建日期: 2025/3/31
版本: 1.0
描述: 字母在字符串中的百分比。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from collections import Counter


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = Counter(s)
        ans = cnt[letter] / len(s) * 100
        print(ans)
        return int(ans)


if __name__ == '__main__':
    sol = Solution()
    print(sol.percentageLetter(s = "foobar", letter = "o"))