#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2743.py
作者: Bolun Xu
创建日期: 2025/3/18
版本: 1.0
描述: 计算没有重复字符的子字符串数量。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter


class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        cnt = Counter()
        ans = 0
        left = 0
        for right, char in enumerate(s):
            cnt[char] += 1

            while max(cnt.values()) > 1:
                cnt[s[left]] -= 1
                left += 1

            ans += right - left + 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSpecialSubstrings("abcd"))
