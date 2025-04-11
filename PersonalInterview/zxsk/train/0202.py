#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0202.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 打字。
"""
def min_key_presses(s):
    uppercase_mode = False
    key_presses = 0
    for char in s:
        if char.isupper() != uppercase_mode:
            key_presses += 1
            uppercase_mode = not uppercase_mode
        key_presses += 1
    return key_presses

# 主程序
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = input().strip()
        print(min_key_presses(s))