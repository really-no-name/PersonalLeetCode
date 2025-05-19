#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3024.py
作者: Bolun Xu
创建日期: 2025/5/19
版本: 1.0
描述: 三角形类型。
时间复杂度： O(1)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[1] + nums[2] > nums[0]:
            if nums[0] == nums[1] and nums[1] == nums[2]:
                return 'equilateral'
            elif nums[0] != nums[1] and nums[1] != nums[2] and nums[2] != nums[0]:
                return 'scalene'
            else:
                return 'isosceles'
        else:
            return 'none'


if __name__ == '__main__':
    sol = Solution()
    print(sol.triangleType([3, 3, 3]))
