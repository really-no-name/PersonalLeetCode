#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0633.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 平方数之和。
时间复杂度： O(Sqrt(C))
空间复杂度： O(1)
"""
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = math.isqrt(c)
        while left < right:
            s = left ** 2 + right ** 2
            if s > c:
                right -= 1
            elif s < c:
                left += 1
            elif s == c:
                print(f"{left} {right}")
                return True
        if left == right and 2 * left * left == c:
            print(f"{left} {right}")
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.judgeSquareSum(5))