#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 检查一个数是否在数组中占绝大多数。
时间复杂度： O(NLogN)
空间复杂度： O(LogN)
执行用时： 0 ms
消耗内存： 17.63 mb
"""
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        nums.sort()
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        return (right - left) > 0.5 * len(nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isMajorityElement(nums=[2, 4, 5, 5, 5, 5, 5, 6, 6], target=5))
