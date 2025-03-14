#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 一维数组的动态和。
时间复杂度： O(N)
空间复杂度： O(1)
执行用时： 0 ms
消耗内存： 17.82 mb
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.runningSum([1, 2, 3, 4]))

