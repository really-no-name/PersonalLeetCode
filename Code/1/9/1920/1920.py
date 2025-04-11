#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1920.py
作者: Bolun Xu
创建日期: 2025/4/11
版本: 1.0
描述: 基于排列构建数组。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            print(nums[i])
            print(nums[nums[i]])
            ans.append(nums[nums[i]])
        return ans