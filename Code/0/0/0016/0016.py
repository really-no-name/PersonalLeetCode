#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0016.py
作者: Bolun Xu
创建日期: 2025/3/24
版本: 1.0
描述: 最接近的三数之和。
时间复杂度： O(N^2)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 2 * 10 ** 4
        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    return s
                if s > target:
                    if s - target < diff:  # s 与 target 更近
                        diff = s - target
                        ans = s
                    right -= 1
                else:  # s < target
                    if target - s < diff:  # s 与 target 更近
                        diff = target - s
                        ans = s
                    left += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
