#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0930.py
作者: Bolun Xu
创建日期: 2025/3/19
版本: 1.0
描述: 和相同的二元子数组。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def numSubarrays(self, nums: List[int], goal: int) -> int:
        """
        统计并返回有多少个和 小于等于 goal 的 非空 子数组
        """
        ans = 0
        window_sum = 0
        left = 0
        for right, num in enumerate(nums):
            window_sum += num

            while window_sum > goal:
                window_sum -= nums[left]
                left += 1

            ans += right - left + 1

        return ans

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        统计并返回有多少个和为 goal 的 非空 子数组
        """
        upper = self.numSubarrays(nums, goal)
        # print(upper)
        if goal - 1 < 0:
            return upper
        else:
            lower = self.numSubarrays(nums, goal - 1)
            # print(lower)
            return upper - lower


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))
    print(solution.numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))
