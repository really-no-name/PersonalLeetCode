#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 整数的各位积和之差。
时间复杂度： O(LogN)
空间复杂度： O(1)

"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        for i in str(n):
            sum += int(i)
            product *= int(i)
        return product - sum


if __name__ == '__main__':
    sol = Solution()
    print(sol.subtractProductAndSum(234))
