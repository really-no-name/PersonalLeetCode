#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 2 的幂。
时间复杂度： O(1)
空间复杂度： O(1)

"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            if n & (n - 1) == 0:
                return True
        return False


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(2))
    print(Solution().isPowerOfTwo(32769))