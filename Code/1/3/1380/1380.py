#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1380.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 矩阵中的幸运数。
时间复杂度： O(Mn)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        lucky_numbers = []  # 存储幸运数的列表

        # 遍历矩阵的每一行
        for row in matrix:
            # 找到当前行的最小值
            min_in_row = min(row)
            # 找到最小值所在的列索引
            min_col_index = row.index(min_in_row)

            # 找到该列的最大值
            column = [r[min_col_index] for r in matrix]  # 获取整列
            max_in_col = max(column)

            # 检查是否满足幸运数条件(既是行最小又是列最大)
            if min_in_row == max_in_col:
                lucky_numbers.append(min_in_row)

        return lucky_numbers


if __name__ == '__main__':
    sol = Solution()
    print(sol.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))