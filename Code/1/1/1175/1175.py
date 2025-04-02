#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1175.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 质数排列。
时间复杂度： O(NLog(LogN))
空间复杂度： O(N)
"""
import math


class Solution:
    def count_primes_sieve(self, n):

        if n < 2:
            return 0

        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        return sum(is_prime)

    def numPrimeArrangements(self, n: int) -> int:
        ans = math.factorial(self.count_primes_sieve(n)) * math.factorial(n - self.count_primes_sieve(n))
        return ans % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numPrimeArrangements(100))