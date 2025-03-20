#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0977.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 有序数组的平方。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         """
#         时间复杂度： O(Nlogn)
#         空间复杂度： O(N)
#         """
#         for i in range(len(nums)):
#             nums[i] = nums[i] ** 2
#         return sorted(nums)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = []
        while left < right:
            x = nums[left] ** 2
            y = nums[right] ** 2
            if x > y:
                ans = [x] + ans
                left += 1
            else:
                ans = [y] + ans
                right -= 1
        if left == right:
            ans = [nums[left] ** 2] + ans
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))
