#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2011.py
作者: Bolun Xu
创建日期: 2025/4/13
版本: 1.0
描述: 执行操作后的变量值。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for operation in operations:
            if operation == '--X' or operation == 'X--':
                X -= 1
            else:
                X += 1
        return X