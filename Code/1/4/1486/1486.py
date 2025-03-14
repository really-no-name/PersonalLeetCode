#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 数组异或操作。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        # print(f"DEBUG: nums 的第 0 项为 {start}")
        for i in range(1, n):
            # print(f"DEBUG: nums 的第 {i} 项为 {start + 2 * i}")
            ans = ans ^ (start + 2 * i)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.xorOperation(5, 0))
    print(sol.xorOperation(4, 3))
    print(sol.xorOperation(1, 7))
    print(sol.xorOperation(10, 5))
