#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3258.py
作者: Bolun Xu
创建日期: 2025/3/18
版本: 1.0
描述: 统计满足 K 约束的子字符串数量 I。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from collections import Counter


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt = Counter()
        ans = 0
        left = 0
        for right, char in enumerate(s):
            cnt[char] += 1

            while cnt['0'] > k and cnt['1'] > k:
                cnt[s[left]] -= 1
                left += 1
            ans += right - left + 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countKConstraintSubstrings(s="10101", k=1))
