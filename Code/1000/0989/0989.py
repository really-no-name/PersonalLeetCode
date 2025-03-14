#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0989.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 数组形式的整数加法。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # number = int(''.join(map(str, num)))
        # return list(map(int, str(number + k)))

        # 将数组形式的整数转换为数字
        num_as_int = 0
        for digit in num:
            num_as_int = num_as_int * 10 + digit

        # 将 k 与转换后的数字相加
        total = num_as_int + k

        # 将相加后的结果转换回数组形式
        result = []
        while total > 0:
            result.append(total % 10)
            total = total // 10

        # 如果结果是 0，直接返回 [0]
        if not result:
            return [0]

        # 反转数组，得到正确的顺序
        return result[::-1]