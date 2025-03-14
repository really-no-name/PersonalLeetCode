#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 和有限的最长子序列。
时间复杂度：O(Nlogn+Mlogn)
空间复杂度：O(1)
执行用时：7 ms
消耗内存：17.78 mb
"""
import bisect
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        ans = [0] * len(queries)
        for i in range(len(queries)):
            ans[i] = bisect.bisect_right(nums, queries[i])
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.answerQueries(nums=[4, 5, 2, 1], queries=[3, 10, 21]))
