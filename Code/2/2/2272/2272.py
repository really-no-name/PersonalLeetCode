#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2272.py
作者: Bolun Xu
创建日期: 2025/3/16
版本: 1.0 -- 暴力循环
描述: 最大波动的子字符串。
时间复杂度：
空间复杂度：
"""
from collections import Counter


class Solution:
    def largestVariance(self, s: str) -> int:
        # 如果所有字符的频率都是1，直接返回0
        if max(Counter(s).values()) == 1:
            return 0

        ans = 0
        for i in range(len(s)):
            # print(f"DEBUG: {s[i]}")
            for j in range(i + 1, len(s)):
                # print(f"DEBUG: {s[j]}")
                cnt = Counter(s[i:j + 1])
                # print(f"DEBUG: {s[i:j + 1]}")
                # print(f"DEBUG: {cnt}")
                ans = max(ans, max(cnt.values()) - min(cnt.values()))

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestVariance("abcdefga"))
