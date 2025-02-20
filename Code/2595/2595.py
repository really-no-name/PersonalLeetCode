#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 这个文件用于演示Python文件模板的常用结构。
时间复杂度： O(LogN)
空间复杂度： O(LogN)
执行用时： 3 ms
消耗内存： 17.6 mb
"""
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        n_2 = bin(n)[2:]
        print(f"Debug: n 的二进制 {n_2}")

        # n_list = list(map(int, str(n_2)))  # 下标从右侧数 ！！！
        n_list = [int (digit) for digit in str(n_2)[::-1]]
        print(f"Debug: n 的二进制列表 {n_list}")
        odd, even = 0, 0
        for i in range(len(n_list)):
            if n_list[i] == 1 and i % 2 == 0:  # 偶数下标
                even += 1
            elif n_list[i] == 1 and i % 2 != 0:  # 奇数下标
                odd += 1

        ans = [even, odd]
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.evenOddBit(50))
    print(sol.evenOddBit(2))
    print(sol.evenOddBit(5))
