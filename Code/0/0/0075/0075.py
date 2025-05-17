#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0075.py
作者: Bolun Xu
创建日期: 2025/5/17
版本: 1.0
描述: 颜色分类。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            elif nums[mid] == 1:
                mid += 1


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)
    print(nums)