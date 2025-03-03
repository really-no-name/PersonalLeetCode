#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0209.py
作者: Bolun Xu
创建日期: 2025/3/3
版本: 1.0
描述: 长度最小的子数组。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [nums_l, nums_l+1, ..., nums_r-1, nums_r]
        :param target: 正整数
        :param nums: 含有 n 个正整数的数组
        :return: 返回其长度。如果不存在符合条件的子数组，返回 0
        """
        ans = len(nums) + 1
        left = 0
        window_sum = 0
        for right, num in enumerate(nums):
            # print(f"DEBUG: number {num} entry the window")
            window_sum += num
            # print(f"DEBUG: the sum of numbers in window {window_sum}")
            while window_sum >= target:
                ans = min(ans, right - left + 1)
                # print(f"DEBUG: the ans is {ans}")
                window_sum -= nums[left]
                # print(f"DEBUG: number {nums[left]} leave the window, and the sum of numbers in window {window_sum}")
                left += 1
        return ans if ans <= len(nums) else 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
    print(solution.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
