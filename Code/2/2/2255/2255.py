#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2255.py
作者: Bolun Xu
创建日期: 2025/3/24
版本: 1.0
描述: 统计是给定字符串前缀的字符串数目。
时间复杂度： O(N∗M)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = Counter(words)
        # print(f"DEBUG: {cnt}")
        ans = 0
        for i in range(len(s)):
            # print(f"DEBUG: {s[0:i + 1]}")
            ans += cnt[s[0:i + 1]]
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrefixes(words=["a", "b", "c", "ab", "bc", "abc"], s="abc"))
