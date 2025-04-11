#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0401.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
from typing import List


def max_1(length: int, k: int, arr: List[int]) -> int:
    left = 0
    max_len = 0
    cnt_0 = 0
    for right in range(length):
        if arr[right] == 0:
            cnt_0 += 1

        while cnt_0 > k:
            if arr[left] == 0:
                cnt_0 -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == '__main__':
    l, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(max_1(l, k, nums))