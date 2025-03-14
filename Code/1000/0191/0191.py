#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 位1的个数。
时间复杂度： O(LogN)
空间复杂度： O(LogN)

"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]  # 转换成二进制
        n = str(n)
        return n.count('1')


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(2147483645))
