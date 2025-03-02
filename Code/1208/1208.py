#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1208.py
作者: Bolun Xu
创建日期: 2025/3/2
版本: 1.0
描述: 尽可能使字符串相等。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [0] * len(s)
        for i in range(len(s)):
            cost[i] = abs(ord(t[i]) - ord(s[i]))
        # print(cost)

        ans = 0
        sumcost = 0
        left = 0
        for right, c in enumerate(cost):
            sumcost += c
            # print(sumcost)
            while sumcost > maxCost:
                sumcost -= cost[left]
                left += 1

            ans = max(ans, right - left + 1)

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.equalSubstring(s="abcd", t="bcdf", maxCost=3))
    print(sol.equalSubstring(s="abcd", t="cdef", maxCost=3))
