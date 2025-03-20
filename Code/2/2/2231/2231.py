#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2231.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 按奇偶性交换后的最大数字。
时间复杂度： O(Nlogn)
空间复杂度： O(N)
"""


class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []
        for n in str(num):
            if int(n) % 2 == 0:
                even.append(int(n))
            else:
                odd.append(int(n))
        odd = sorted(odd)
        even = sorted(even)
        print(odd)
        print(even)
        ans = ''
        for n in str(num):
            if int(n) % 2 == 0:
                ans += str(even[-1])
                even.pop(-1)
            else:
                ans += str(odd[-1])
                odd.pop(-1)
        return int(ans)


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestInteger(123))