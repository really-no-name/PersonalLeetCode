#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 各位相加。
时间复杂度： O(1)
空间复杂度： O(1)

"""


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return (num - 1) % 9 + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.addDigits(38))
