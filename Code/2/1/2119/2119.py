#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2119.py
作者: Bolun Xu
创建日期: 2025/3/29
版本: 1.0
描述: 反转两次的数字。
时间复杂度： O(N)
空间复杂度： O(N)
"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True

        str_num = str(num)
        if str_num[-1] == "0":
            return False
        else:
            return True
