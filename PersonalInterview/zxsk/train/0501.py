#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0501.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def can_be_palindrome(s: str) -> str:
    for i in range(len(s) + 1):
        for char in 'qwertyuiopasdfghjklzxcvbnm':
            new_s = s[:i] + char + s[i:]
            if is_palindrome(new_s):
                return 'Yes'
    return 'No'


if __name__ == '__main__':
    s = input().strip()  # 字符串输入
    print(can_be_palindrome(s))