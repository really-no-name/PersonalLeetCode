#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0201.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 【输入】读取未给出行列数的矩阵。
"""
import sys


def main():
    # 从标准输入读取所有行，strip去除空行
    matrix = [list(map(int, line.strip().split())) for line in sys.stdin if line.strip()]  # 矩阵输入

    # 判断是否为空矩阵
    if not matrix:
        return

    # 转置矩阵并打印
    transposed = zip(*matrix)
    for row in transposed:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    main()