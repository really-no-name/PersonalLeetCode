#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0136.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 只出现一次的数字。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)