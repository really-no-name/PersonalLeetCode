#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2996.py
作者: Bolun Xu
创建日期: 2025/4/7
版本: 1.0
描述: 大于等于顺序前缀和的最小缺失整数。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def sequentialPrefixSum(self, nums:List[int]) -> int:
        """
        返回最长顺序前缀的和
        """
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                ans += nums[i]
            else:
                break
        # print(F"DEBUG: {ans}")
        return ans

    def missingInteger(self, nums: List[int]) -> int:
        prefixSum = self.sequentialPrefixSum(nums)
        while True:
            if prefixSum not in nums:
                return prefixSum
            else:
                prefixSum += 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.missingInteger([4,5,6,7,8,8,9,4,3,2,7]))