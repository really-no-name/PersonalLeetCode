#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2012.py
作者: Bolun Xu
创建日期: 2025/3/11
版本: 1.0
描述: 数组美丽值求和。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)

        # 计算 prefix_max
        prefix_max = nums[0]
        print(f"DEBUG: {prefix_max}")

        # 计算 suffix_min
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, 1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
        print(f"DEBUG: {suffix_min}")

        ans = 0
        for i in range(1, n - 1):
            num = nums[i]
            if prefix_max < num < suffix_min[i + 1]:
                ans += 2
            elif nums[i - 1] < num < nums[i + 1]:
                ans += 1
            prefix_max = max(prefix_max, num)
            print(f"DEBUG: {prefix_max}")
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfBeauties([1,2,3]))


