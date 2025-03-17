#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0738.py
作者: Bolun Xu
创建日期: 2025/3/17
版本: 1.0 -- 超出时间限制
描述: 单调递增的数字。
时间复杂度：
空间复杂度：
"""


class Solution:
    def is_monotonic_increasing(self, number: int) -> bool:
        # 将数字转换为字符串，方便逐个比较
        num_str = str(number)

        # 遍历字符串，比较相邻的数字
        for i in range(len(num_str) - 1):
            if num_str[i] > num_str[i + 1]:
                return False

        # 如果所有相邻数字都满足 x <= y，返回 True
        return True

    def monotoneIncreasingDigits(self, n: int) -> int:
        while True:
            if self.is_monotonic_increasing(n):
                return n
            else:
                n -= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.monotoneIncreasingDigits(10))