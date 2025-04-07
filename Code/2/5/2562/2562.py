#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2562.py
作者: Bolun Xu
创建日期: 2025/4/7
版本: 1.0
描述: 找出数组的串联值。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            ans += int(str(nums[left]) + str(nums[right]))
            # print(int(str(nums[left]) + str(nums[right])))
            left += 1
            right -= 1
        if left == right:
            ans += nums[left]
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findTheArrayConcVal([5,14,13,8,12]))
