#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 各位相加 -- 硬循环。
时间复杂度： O(Logn)
空间复杂度： O(Logn)

"""


class Solution:
    def addDigits(self, num: int) -> int:
        def dfs(n: int) -> int:
            s = 0
            for i in str(n):
                s += int(i)
            n = s

            if n < 10:
                # print(num)
                return n
            else:
                return dfs(n)

        ans = dfs(num)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.addDigits(38))
