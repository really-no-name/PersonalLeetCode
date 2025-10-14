#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3349.py
作者: Bolun Xu
创建日期: 2025/10/14
版本: 1.0
描述: 检测相邻递增子数组 I。
时间复杂度： O(Nk)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                continue
            else:
                return False
        return True

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2 * k:
            return False
        for i in range(0, len(nums) - 2 * k + 1):
            # print(nums[i])
            # print(nums[i : i + k], self.check(nums[i : i + k]))
            # print(nums[i + k : i + 2 * k], self.check(nums[i + k : i + 2 * k]))
            if self.check(nums[i : i + k]) and self.check(nums[i + k : i + 2 * k]):
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.hasIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1], k = 3))