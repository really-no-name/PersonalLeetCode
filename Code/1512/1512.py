#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 好数对的数目。
时间复杂度： O(N ^2 )
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
