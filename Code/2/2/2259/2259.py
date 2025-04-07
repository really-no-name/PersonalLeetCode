#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2259.py
作者: Bolun Xu
创建日期: 2025/4/7
版本: 1.0
描述: 移除指定数字得到的最大结果。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0
        for i, num in enumerate(number):
            if num == digit:
                # print(f"DEBUG: {number[:i] + number[i+1:]}")
                ans = max(ans, int(number[:i] + number[i+1:]))
        return str(ans)


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDigit(number = "12131", digit = "1"))