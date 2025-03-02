#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1695.py
作者: Bolun Xu
创建日期: 2025/3/2
版本: 1.0
描述: 删除子数组的最大得分。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        从一个正整数数组 nums 中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和.
        :param nums:
        :return: 返回 只删除一个 子数组可获得的 最大得分 。
        """
        ans = 0
        left = 0
        count = Counter()
        s = 0
        for right, num in enumerate(nums):
            # print(f"\nDEBUG: Processing element at index {right}: {num}")
            s += num
            count[num] += 1
            # print(f"DEBUG: Current window: {nums[left:right + 1]}")
            # print(f"DEBUG: Current sum: {s}")
            # print(f"DEBUG: Current count: {count}")

            while count[num] > 1:
                # print(f"DEBUG: Duplicate found: {num} appears {count[num]} times")
                # print(f"DEBUG: Moving left pointer from {left} to {left + 1}")
                count[nums[left]] -= 1
                s -= nums[left]
                left += 1
                # print(f"DEBUG: Updated window: {nums[left:right + 1]}")
                # print(f"DEBUG: Updated sum: {s}")
                # print(f"DEBUG: Updated count: {count}")

            ans = max(ans, s)
            # print(f"DEBUG: Current maximum score: {ans}")

        # print(f"\nDEBUG: Final maximum score: {ans}")
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumUniqueSubarray([4,2,4,5,6]))