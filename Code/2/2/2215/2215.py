#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2215.py
作者: Bolun Xu
创建日期: 2025/4/16
版本: 1.0
描述: 找出两数组的不同。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1 = set(nums1) - (set(nums1) & set(nums2))
        l2 = set(nums2) - (set(nums1) & set(nums2))
        return [list(l1), list(l2)]