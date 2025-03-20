#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0168.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: Excel 表列名称。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # 因为 Excel 列名称是从 1 开始的
            remainder = columnNumber % 26
            result = chr(65 + remainder) + result
            print(result)
            columnNumber = columnNumber // 26
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToTitle(28))
    print(solution.convertToTitle(2147483647))
