#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2293.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 极大极小游戏。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        def dfs(nums: List[int]) -> List[int]:
            if len(nums) == 1:
                return nums

            state = -1
            result = []
            for i in range(0, len(nums), 2):
                if state == -1:
                    result.append(min(nums[i], nums[i + 1]))
                elif state == 1:
                    result.append(max(nums[i], nums[i + 1]))
                state *= -1
            return dfs(result)

        return dfs(nums)[0]