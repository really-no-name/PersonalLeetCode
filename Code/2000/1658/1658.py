#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1658.py
作者: Bolun Xu
创建日期: 2025/3/3
版本: 1.0
描述: 将 x 减到 0 的最小操作数。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。
        :param nums: 整数数组
        :param x: 整数
        :return: 如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。
        """
        window_sum = sum(nums) - x
        if window_sum < 0:
            return -1  # 全部移除也无法满足要求

        answer = -1
        left = 0
        s = 0
        # cnt = Counter()
        for right, num in enumerate(nums):
            s += num
            # cnt[num] += 1

            while s > window_sum:
                s -= nums[left]
                # cnt[nums[left]] -= 1
                left += 1
            if s == window_sum:
                answer = max(answer, right - left + 1)
        return -1 if answer < 0 else len(nums) - answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.minOperations(nums=[1, 1, 4, 2, 3], x=5))
    print(solution.minOperations(nums = [5,6,7,8,9], x = 4))
    print(solution.minOperations(nums = [3,2,20,1,1,3], x = 10))
