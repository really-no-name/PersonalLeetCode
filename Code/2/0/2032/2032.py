#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2032.py
作者: Bolun Xu
创建日期: 2025/4/13
版本: 1.0
描述: 至少在两个数组中出现的值。
时间复杂度： O(N+M+P)
空间复杂度： O(N+M+P)
"""
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        l1 = list(set(nums1) & set(nums2))
        l2 = list(set(nums2) & set(nums3))
        l3 = list(set(nums1) & set(nums3))
        return list(set(l1 + l2 + l3))