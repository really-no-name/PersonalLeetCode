#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 2 的幂 —— 复杂写法。
时间复杂度： O(Logn)
空间复杂度： O(Logn)

"""
import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        n_2 = bin(abs(n))[2:]  # 转换成 2 进制
        n_2 = int(n_2)
        # print(f"DEBUG: Binary system: {n_2}")
        # 将数字转换为字符串
        s = str(n_2)
        # 检查是否只有一个 '1' 和若干个 '0'
        return s.count('1') == 1 and s.count('0') == len(s) - 1


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(2))
    print(Solution().isPowerOfTwo(32769))

