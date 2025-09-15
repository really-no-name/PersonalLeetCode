#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1935.py
作者: Bolun Xu
创建日期: 2025/9/15
版本: 1.0
描述: 可以输入的最大单词数。
时间复杂度： O(N)
空间复杂度： O(N)
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_list = text.split()
        # print(text_list)
        cnt = 0
        for word in text_list:
            if set(word) & set(brokenLetters):
                # print(word)
                continue
            else:
                cnt += 1

        return cnt


if __name__ == '__main__':
    sol = Solution()
    print(sol.canBeTypedWords(text = "hello world", brokenLetters = "ad"))
    print(sol.canBeTypedWords(text = "leet code", brokenLetters = "e"))