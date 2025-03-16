#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1358.py
作者: Bolun Xu
创建日期: 2025/3/16
版本: 1.0
描述: 包含所有三种字符的子字符串数目。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        ans = 0
        cnt = defaultdict(int)
        for right, letter in enumerate(s):
            cnt[letter] += 1

            while len(cnt) == 3:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            ans += left

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSubstrings('abcabc'))
