#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0601.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
from typing import List
from itertools import permutations, product

# 所有操作
ops = ['+', '-', '*', '/']


def calc(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/':
        if b == 0: return None
        return a / b


def check(nums: List[int]) -> str:
    for num_perm in permutations(nums):
        a, b, c, d = num_perm
        for op1, op2, op3 in product(ops, repeat=3):
            try:
                # 5种括号组合方式
                res1 = calc(calc(calc(a, b, op1), c, op2), d, op3)
                res2 = calc(calc(a, calc(b, c, op2), op1), d, op3)
                res3 = calc(a, calc(calc(b, c, op2), d, op3), op1)
                res4 = calc(a, calc(b, calc(c, d, op3), op2), op1)
                res5 = calc(calc(a, b, op1), calc(c, d, op3), op2)
                for res in [res1, res2, res3, res4, res5]:
                    if res is not None and abs(res - 24) < 1e-6:
                        return 'yes'
            except:
                continue
    return 'no'



if __name__ == '__main__':
    lim = int(input())
    for _ in range(lim):
        print(check(list(map(int, input().split()))))

