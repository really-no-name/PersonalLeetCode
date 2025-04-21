#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0283.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 2.0
描述: 移动零。
时间复杂度： O(N^2)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt0 = 0
        while True:
            try:
                nums.remove(0)
                cnt0 += 1
            except ValueError:
                break
        nums += [0] * cnt0


if __name__ == '__main__':
    sol = Solution()
    l = [0,1,0,3,12]
    sol.moveZeroes(l)
    print(l)