#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0902.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
def get_difficulty(x, y):
    rate = y / x
    if rate <= 0.3:
        return 5
    elif rate <= 0.6:
        return 4
    else:
        return 3

def main():
    n = int(input())
    problems = []

    for _ in range(n):
        parts = input().split()
        name = parts[0]
        x = int(parts[1])
        y = int(parts[2])
        difficulty = get_difficulty(x, y)
        problems.append((name, difficulty))

    # 按名称字典序排序
    problems.sort()

    # 输出
    for name, difficulty in problems:
        print(f"{name} {difficulty}")

if __name__ == '__main__':
    main()