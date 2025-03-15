#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2090.py
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 半径为 k 的子数组平均值。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)
        l = k * 2 + 1
        s = 0
        for i, num in enumerate(nums):
            s += num
            if i < l - 1:
                continue
            ans[i - k] = int(s / l)
            s -= nums[i - l + 1]
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.getAverages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3))
