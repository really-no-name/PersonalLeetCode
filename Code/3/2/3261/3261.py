#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3261.py
作者: Bolun Xu
创建日期: 2025/3/18
版本: 1.0 -- 超出时间限制
描述: 统计满足 K 约束的子字符串数量 II。
时间复杂度：
空间复杂度：
"""
from collections import Counter
from typing import List


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        ans = []
        for query in queries:
            print(s[query[0]:query[1] + 1])
            ans.append(self.countK(s=s[query[0]:query[1] + 1], k=k))
        return ans

    def countK(self, s: str, k: int) -> int:
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
    print(sol.countKConstraintSubstrings(s="0001111", k=2, queries=[[0, 6]]))
    print(sol.countKConstraintSubstrings(s="010101", k=1, queries=[[0, 5], [1, 4], [2, 3]]))
