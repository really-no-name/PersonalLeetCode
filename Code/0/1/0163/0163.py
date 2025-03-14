#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0163.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 缺失的区间。
时间复杂度： O(N)
空间复杂度： O(N)
"""
import bisect
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        perv = lower - 1
        for num in nums:
            if num > perv + 1:
                ans.append([perv + 1, num - 1])
            perv = num
        if perv < upper:
            ans.append([perv + 1, upper])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMissingRanges(nums = [0, 1, 3, 50, 75], lower = 0 , upper = 99))