#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0018.py
作者: Bolun Xu
创建日期: 2025/3/24
版本: 1.0
描述: 四数之和。
时间复杂度： O(N^3)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:  # 跳过重复数字
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # 跳过重复数字
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    window_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if window_sum > target:
                        right -= 1
                    elif window_sum < target:
                        left += 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:  # 跳过重复数字
                            left += 1

                        right -= 1
                        while right > left and nums[right] == nums[right + 1]:  # 跳过重复数字
                            right -= 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
