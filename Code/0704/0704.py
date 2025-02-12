#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: example.py
作者: Bolun Xu
版本: 1.0
描述: 二分查找。
时间复杂度：O(LogN)
空间复杂度：o(1)
执行用时：0 ms
消耗内存：18.58 mb
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums = [-1,0,3,5,9,12], target = 9))