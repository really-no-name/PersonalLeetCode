#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0325.py
作者: Bolun Xu
创建日期: 2025/4/16
版本: 1.0
描述: 和等于 k 的最长子数组长度。
时间复杂度：
空间复杂度：
"""
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = {}  # key: prefix_sum, value: the earliest index where this sum occurs
        current_sum = 0
        max_len = 0

        print(f"Input array: {nums}, target k: {k}")
        print("=" * 50)

        for i in range(len(nums)):
            current_sum += nums[i]
            print(f"\nStep {i}: nums[{i}] = {nums[i]}")
            print(f"Current prefix sum (sum from 0 to {i}): {current_sum}")

            # Case 1: The subarray from 0 to i sums to k
            if current_sum == k:
                max_len = i + 1
                print(f"Found sum=k from index 0 to {i}, update max_len to {max_len}")

            # Case 2: Check if (current_sum - k) exists in prefix_sum
            if (current_sum - k) in prefix_sum:
                start_index = prefix_sum[current_sum - k]
                current_subarray_len = i - start_index
                print(f"Found sum=k from index {start_index + 1} to {i} (len={current_subarray_len})")
                max_len = max(max_len, current_subarray_len)
                print(f"Update max_len to {max_len}")

            # Only store the first occurrence of each prefix_sum to get the longest subarray
            if current_sum not in prefix_sum:
                prefix_sum[current_sum] = i
                print(f"First time seeing prefix_sum={current_sum}, store in prefix_sum with index {i}")
            else:
                print(f"prefix_sum={current_sum} already exists at index {prefix_sum[current_sum]}, skip storing")

            print(f"Current prefix_sum dict: {prefix_sum}")
            print(f"Current max_len: {max_len}")

        print("\nFinal result:")
        return max_len


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3))
