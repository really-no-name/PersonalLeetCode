#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2273.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 移除字母异位词后的结果数组。
时间复杂度： O(Nklogk)
空间复杂度： O(Nk)
"""
from collections import Counter
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if not words:
            return []

        result = [words[0]]
        for i in range(1, len(words)):
            if Counter(words[i]) != Counter(result[-1]):
                result.append(words[i])

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeAnagrams(["abba","baba","bbaa","cd","cd"]))