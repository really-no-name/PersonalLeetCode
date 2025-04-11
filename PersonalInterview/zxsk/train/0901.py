#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0901.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
def find_kth_largest(n, k, A, B, C):
    total = A + B + C
    total.sort()
    return total[k - 1]

# 主程序
if __name__ == '__main__':
    n, k = map(int, input().split())
    A = list(map(int, input().split()))  # 使用空格分割，list输入
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(find_kth_largest(n, k, A, B, C))