#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1328.py
作者: Bolun Xu
创建日期: 2025/3/5
版本: 1.0
描述: 破坏回文串。
时间复杂度：
空间复杂度：
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """

        :param palindrome:
        :return:
        """
        length = len(palindrome)

        if length <= 1:
            return ""

        for i in range(length // 2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i + 1:]
        return palindrome[:-1] + "b"


if __name__ == '__main__':
    sol = Solution()
    print(sol.breakPalindrome("abcba"))
