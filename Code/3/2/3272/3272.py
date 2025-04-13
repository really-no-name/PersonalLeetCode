#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3272.py
作者: Bolun Xu
创建日期: 2025/4/13
版本: 1.0
描述: 统计好整数的数目。
时间复杂度：
空间复杂度：
"""
from collections import Counter
from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        vis = set()
        base = 10 ** ((n - 1) // 2)
        for i in range(base, base * 10):  # 枚举回文数左半边
            s = str(i)
            s += s[::-1][n % 2:]
            if int(s) % k:  # 回文数不能被 k 整除
                continue

            sorted_s = ''.join(sorted(s))
            if sorted_s in vis:  # 不能重复统计
                continue
            vis.add(sorted_s)

            cnt = Counter(sorted_s)
            res = (n - cnt['0']) * fac[n - 1]
            for c in cnt.values():
                res //= fac[c]
            ans += res
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countGoodIntegers(n = 3, k = 5))