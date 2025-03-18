#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode LCP_068.py
作者: Bolun Xu
创建日期: 2025/3/18
版本: 1.0
描述: 美观的花束。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        count = Counter()
        ans = 0
        left = 0
        for right, flower in enumerate(flowers):
            count[flower] += 1

            while max(count.values()) > cnt:
                count[flowers[left]] -= 1
                left += 1

            ans += right - left + 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.beautifulBouquet(flowers=[1, 2, 3, 2], cnt=1))
