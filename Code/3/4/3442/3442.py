#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3442.py
作者: Bolun Xu
创建日期: 2025/6/10
版本: 1.0
描述: 奇偶频次间的最大差值 I。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from math import inf


class Solution:
    def maxDifference(self, s: str) -> int:
        # 奇数最大，最小正偶数
        counter = Counter(s)
        print(counter)
        max_odd = 0
        min_even = inf
        for key in counter.keys():
            if counter[key] % 2 == 0:
                min_even = min(min_even, counter[key])
            else:
                max_odd = max(max_odd, counter[key])
        print(max_odd, min_even)
        return max_odd - min_even


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxDifference("aaaaabbc"))
    print(sol.maxDifference("mmsmsym"))