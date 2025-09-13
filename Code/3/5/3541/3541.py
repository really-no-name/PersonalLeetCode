#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3541.py
作者: Bolun Xu
创建日期: 2025/9/13
版本: 1.0
描述: 找到频率最高的元音和辅音。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = Counter(s)
        max_vowel = 0
        max_consonant = 0
        for char in cnt.keys():
            if char in 'aeiou':
                max_vowel = max(max_vowel, cnt[char])
            else:
                max_consonant = max(max_consonant, cnt[char])
        return max_vowel + max_consonant


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxFreqSum("successes"))