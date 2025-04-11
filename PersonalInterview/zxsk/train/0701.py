#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0701.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
import math


def loc(L: int, R: int) -> None:
    theta = L / R

    # 顺时针
    x1 = R * math.cos(- theta)
    y1 = R * math.sin(- theta)

    # 逆时针
    x2 = R * math.cos(theta)
    y2 = R * math.sin(theta)

    print(f"{x1:.3f} {y1:.3f}")
    print(f"{x2:.3f} {y2:.3f}")


if __name__ == '__main__':
    L, R = map(int, input().split())
    loc(L, R)
