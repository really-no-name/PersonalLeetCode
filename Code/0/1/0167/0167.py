#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 两数之和 II - 输入有序数组。
时间复杂度：
空间复杂度：
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(nums) - 1
        while left_index < right_index:
            s = nums[left_index] + nums[right_index]
            if s == target:
                break
            elif s < target:
                left_index += 1
            else:
                right_index -= 1
        return [left_index + 1, right_index + 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
