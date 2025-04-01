#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1974.py
作者: Bolun Xu
创建日期: 2025/4/1
版本: 1.0
描述: 使用特殊打字机键入单词的最少时间。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 1  # 初始为 'a'
        # print(f"DEBUG: move from a to {word[0]}")
        ans += min(abs(ord(word[0]) - ord('a')), 26 - abs(ord(word[0]) - ord('a')))
        for i in range(1, len(word)):
            # print(f"DEBUG: move from {word[i - 1]} to {word[i]}")
            # print(f"DEBUG: 顺时针转 {abs(ord(word[i]) - ord(word[i - 1]))}")
            # print(f"DEBUG: 逆时针转 {26 - abs(ord(word[i]) - ord(word[i - 1]))}")
            ans += min(abs(ord(word[i]) - ord(word[i - 1])), 26 - abs(ord(word[i]) - ord(word[i - 1])))
            ans += 1  # 敲下当前字符
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.minTimeToType("zjpc"))