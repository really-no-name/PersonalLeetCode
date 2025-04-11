#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0907.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
from typing import List


def is_lucky_sequence(line):
    parts = list(map(int, line.strip().split()))
    n = parts[0]
    A = parts[1:]

    if len(A) != n:
        return "Unluck sequence"

    jump_set = set(abs(A[i] - A[i - 1]) for i in range(1, n))
    required = set(range(1, n))

    return "Luck sequence" if jump_set == required else "Unluck sequence"

# 主程序：支持多行输入直到EOF
if __name__ == '__main__':
    import sys
    for line in sys.stdin:
        if line.strip():
            print(is_lucky_sequence(line))