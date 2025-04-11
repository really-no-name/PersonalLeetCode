#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0908.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
from typing import List
from functools import cmp_to_key

def compare(a: str, b: str) -> int:
    if a + b > b + a:
        return -1
    else:
        return 1

def solution(nums: List[str]) -> None:
    nums.sort(key=cmp_to_key(compare))
    print(''.join(nums))

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(str, input().split()))
    solution(numbers)