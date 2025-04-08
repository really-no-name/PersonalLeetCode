#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1752.py
作者: Bolun Xu
创建日期: 2025/4/8
版本: 1.0
描述: 检查数组是否经排序和轮转得到。
时间复杂度： O(Nlogn)
空间复杂度： O(N)
"""
from typing import List



class Solution:
    def check(self, nums: List[int]) -> bool:
        if nums == sorted(nums):
            return True
        split = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                split = i
        new_nums = nums[split + 1:] + nums[:split + 1]
        print(new_nums)
        print(sorted(new_nums))
        return new_nums == sorted(new_nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.check([3,4,5,1,2]))