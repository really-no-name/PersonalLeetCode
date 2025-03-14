#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2841.py
作者: Bolun Xu
创建日期: 2025/2/27
版本: 1.0
描述: 几乎唯一子数组的最大和。
时间复杂度： O(N)
空间复杂度： O(K)
"""
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = 0
        window = []  # 当前窗口
        s = 0  # 当前窗口的和
        for i, num in enumerate(nums):
            # 进入窗口
            window.append(num)
            s += num
            # 窗口长度不足
            if i < k - 1:
                continue
            # 更新最大值
            if len(set(window)) >= m:  # 列表中是否至少有 m 个不重复数字，是几乎唯一子数组
                ans = max(ans, s)
            # 离开窗口
            window = window[1:]
            s -= nums[i - k + 1]
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSum(nums=[2, 6, 7, 3, 1, 7], m=3, k=4))
    print(solution.maxSum(nums=[5, 9, 9, 2, 4, 5, 4], m=1, k=3))
