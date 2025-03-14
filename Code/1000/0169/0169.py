#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 多数元素。
时间复杂度： O(NLogN)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
