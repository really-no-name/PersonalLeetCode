#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2942.py
作者: Bolun Xu
创建日期: 2025/5/24
版本: 1.0
描述: 查找包含给定字符的单词。
时间复杂度： O(N∗M)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "z"))