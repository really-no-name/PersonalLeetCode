#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0560.py
作者: Bolun Xu
创建日期: 2025/3/19
版本: 1.0
描述: 和为 K 的子数组。
时间复杂度：
空间复杂度：
"""
# 滑动窗口需要满足单调性，当右端点元素进入窗口时，窗口元素和是不能减少的。本题 nums 包含负数，当负数进入窗口时，窗口左端点反而要向左移动，
# 不适合用滑动窗口做
from typing import List


# class Solution:
#
#     def subarraySum(self, nums: List[int], k: int) -> int:
#
#
#
# if __name__ == '__main__':
#     solution = Solution()
#     print(solution.subarraySum(nums=[1, 1, 1], k=2))
#     print(solution.subarraySum([-1, -1, 1], 0))
