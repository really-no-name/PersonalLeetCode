#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0349.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 两个数组的交集。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))