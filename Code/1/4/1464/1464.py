#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1464.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 数组中两元素的最大乘积。
时间复杂度： O(Nlogn)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)