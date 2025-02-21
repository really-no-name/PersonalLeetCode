#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 将数字变成 0 的操作次数。
时间复杂度： O(Logn)
空间复杂度： O(1)
执行用时： 0 ms
消耗内存： 17.38 mb
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            step += 1
        return step


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfSteps(14))