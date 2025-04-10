#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1880.py
作者: Bolun Xu
创建日期: 2025/4/10
版本: 1.0
描述: 检查某单词是否等于两单词之和。
时间复杂度： O(N)
空间复杂度： O(N)
"""
class Solution:
    def word2value(self, word: str) -> int:
        ans = ''
        for char in word:
            ans += str(ord(char) - 97)
        return int(ans)

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.word2value(firstWord) + self.word2value(secondWord) == self.word2value(targetWord)