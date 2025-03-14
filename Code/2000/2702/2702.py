#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2702.py
作者: Bolun Xu
创建日期: 2025/3/6
版本: 1.0
描述: 使数字变为非正数的最小操作次数。
时间复杂度： O(NLogM)
空间复杂度： O(1)
"""
import math
from typing import List


class Solution:
    def just(self, nums: List[int], x: int, y: int, k: int) -> bool:
        diff = x - y
        t_x = 0
        for i, num in enumerate(nums):
            if num / y <= k:
                continue
            else:  # num / y > k
                remain = num - y * k
                # t_x += remain / diff
                # t_x += (remain - 1) / diff + 1  # 需要向上取整
                t_x += math.ceil(remain / diff)  # 需要向上取整
        if t_x <= k:
            return True
        else:
            return False

    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        left = 0
        right = max(nums) // y + 1
        while left < right:
            mid = (left + right) // 2
            print(f"DEBUG: left {left}, mid {mid}, right {right}")
            if self.just(nums, x, y, mid):  # 当前值满足
                print(f"DEBUG: 当前值满足")
                right = mid
            else:
                print(f"DEBUG: 当前值不满足")
                left = mid + 1
        return right


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations(nums=[3, 4, 1, 7, 6], x=4, y=2))
    print(sol.minOperations(nums=[1, 2, 1], x=2, y=1))
    print(sol.minOperations(nums=[74, 92, 25, 65, 77, 1, 73], x=10, y=4))
