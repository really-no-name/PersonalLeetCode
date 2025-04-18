#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2325.py
作者: Bolun Xu
创建日期: 2025/4/18
版本: 1.0
描述: 解密消息。
时间复杂度： O(N∗M)
空间复杂度： O(N)
"""


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        password = []
        for char in key:
            if char in password or char == ' ':
                continue
            else:
                password.append(char)
        print(password)
        decode =''
        for char in message:
            if char == ' ':
                decode += ' '
            else:
                decode += chr(password.index(char) + 97)
        return decode


if __name__ == '__main__':
    sol = Solution()
    print(sol.decodeMessage(key = "the quick brown fox jumps over the lazy dog",
                            message = "vkbs bs t suepuv"))  # return "this is a secret"