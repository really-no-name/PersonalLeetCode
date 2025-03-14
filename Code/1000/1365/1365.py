#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 有多少小于当前数字的数字。
时间复杂度： O(NLogN)
空间复杂度： O(N)
执行用时： 0 ms
消耗内存： 17.50 mb
"""
import bisect
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        # print(f"Debug: 排序后的 nums: {sorted_nums}")
        ans = [0] * len(nums)
        for idx, num in enumerate(nums):
            # print(f"Debug: 当前查找: {num}")
            ans[idx] = bisect.bisect_left(sorted_nums, num)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
