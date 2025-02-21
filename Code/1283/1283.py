#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 使结果不超过阈值的最小除数。
时间复杂度： O(Log(N))
空间复杂度： O(N)
执行用时： 1233 ms
消耗内存： 22.10 mb
"""
import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1  # 除数最小为1
        right = max(nums)
        print(f"Debug: Initial left: {left}, right: {right}")

        while left < right:
            mid = (left + right) // 2
            total = self.divsum(nums, mid)
            print(f"Debug: mid: {mid}, and the division sum is {total}")
            if total <= threshold:
                right = mid  # 尝试更小的除数
            else:
                left = mid + 1  # 需要更大的除数
            print(f"Debug: New bound is: {left}, {right}")
        return left

    def divsum(self, nums: List[int], dividend: int) -> int:
        ans = 0
        for num in nums:
            ans += math.ceil(num / dividend)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestDivisor(nums=[1, 2, 5, 9], threshold=6))
    print(sol.smallestDivisor(nums=[21212, 10101, 12121], threshold=1000000))
