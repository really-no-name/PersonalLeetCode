#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 统计公平数对的数目。
时间复杂度： O(NLogN)
空间复杂度： O(N)
执行用时： 245 ms
消耗内存： 31.04 mb
"""
import bisect
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        print(f"Debug： 排序后的列表 {nums} ")
        ans = 0
        for j, x in enumerate(nums):
            # 注意要在 [0, j) 中二分，因为题目要求两个下标 i < j
            right = bisect.bisect_right(nums, upper - x, 0, j)  # <= upper-nums[j] 的 nums[i] 的个数
            left = bisect.bisect_left(nums, lower - x, 0, j)  # < lower-nums[j] 的 nums[i] 的个数

            print(f"Debug: {x} 的公平数对范围是 {left}到 {right}")
            ans += right - left
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.countFairPairs(nums=[0, 1, 7, 4, 4, 5], lower=3, upper=6))
    print(solution.countFairPairs(nums=[1, 7, 9, 2, 5], lower=11, upper=11))
    print(solution.countFairPairs(nums=[0, 0, 0, 0, 0, 0], lower=0, upper=0))
