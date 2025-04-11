#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0801.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
from typing import List


def digit_sum(n: int) -> int:
    return sum(map(int, str(n)))


def encode(n: int, s: int) -> None:
    min_code = -1
    max_code = -1
    low = 10 ** (n - 1)
    up = 10 ** n - 1

    for num in range(low, up + 1):
        if digit_sum(num) == s:
            min_code = num
            break

    for num in range(up, low - 1, -1):
        if digit_sum(num) == s:
            max_code = num
            break

    if min_code == -1 or max_code == -1:  # 没有找到任何满足条件的数字
        print(-1, -1)
    elif min_code == max_code:  # 只有一个满足条件的数字
        print(-1, -1)
    else:
        print(f"{min_code} {max_code}")


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, s = map(int, input().split())
        encode(n, s)