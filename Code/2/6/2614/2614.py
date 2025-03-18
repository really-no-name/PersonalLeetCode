#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2614.py
作者: Bolun Xu
创建日期: 2025/3/18
版本: 1.0
描述: 对角线上的质数。
时间复杂度： O(N ^ 2 * Sqrt(N))
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def is_prime(self, n):
        if n <= 1:
            return 0
        if n == 2:
            return n
        if n % 2 == 0:
            return 0
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return 0
        return n

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0
        length = len(nums)
        for i in range(length):
            ans = max(ans, self.is_prime(nums[i][i]), self.is_prime(nums[i][length - i - 1]))
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.diagonalPrime([[1, 2, 3], [5, 6, 7], [9, 10, 11]]))
