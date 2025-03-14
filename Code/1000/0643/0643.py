#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 子数组最大平均数 I。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from math import inf
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = -inf
        s = 0
        for i, n in enumerate(nums):
            # 第 i 项 n 进入窗口
            s += n
            # 窗口长度不足
            if i < k - 1:
                continue
            # 更新最大值
            max_sum = max(max_sum, s)
            # 第 i - k + 1 项离开窗口
            s -= nums[i - k + 1]
        return max_sum / k


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
