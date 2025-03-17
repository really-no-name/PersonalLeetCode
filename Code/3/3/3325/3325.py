#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3325.py
作者: Bolun Xu
创建日期: 2025/3/17
版本: 1.0
描述: 字符至少出现 K 次的子字符串 I。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        left = 0
        ans = 0
        for char in s:
            cnt[char] += 1

            while max(cnt.values()) == k:
                cnt[s[left]] -= 1
                left += 1
            ans += left
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSubstrings(s="abacb", k=2))
