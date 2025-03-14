#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 正整数和负整数的最大计数。
时间复杂度：O(N)
空间复杂度：O(1)
执行用时：0 ms
消耗内存：17.66 mb
"""
from typing import List


class Solution:
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # 左闭右开区间
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def maximumCount(self, nums: List[int]) -> int:
        negative = self.lower_bound(nums, 0)
        # print("number of negative: ", negative)
        positive = len(nums) - self.lower_bound(nums, 1)
        # print("number of positive: ", positive)
        return max(negative, positive)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumCount(nums=[-3, -2, -1, 0, 0, 1, 2]))
    print(solution.maximumCount(nums=[-2, -1, -1, 1, 2, 3]))
    print(solution.maximumCount(nums=[5, 20, 66, 1314]))
