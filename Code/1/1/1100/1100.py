#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1100.py
作者: Bolun Xu
创建日期: 2025/2/28
版本: 1.0
描述: 长度为 K 的无重复字符子串。
时间复杂度： O(N)
空间复杂度： O(K)
"""


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        window = ''
        ans = 0
        for i, word in enumerate(s):
            window += word
            if i < k - 1:
                continue
            if len(set(window)) == k:
                ans += 1
            window = window[1:]
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numKLenSubstrNoRepeats(s="havefunonleetcode", k=5))
