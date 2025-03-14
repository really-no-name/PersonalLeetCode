#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1004.py
作者: Bolun Xu
创建日期: 2025/3/3
版本: 1.0
描述: 最大连续1的个数 III。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        :param nums: 二进制数组 nums
        :param k: 整数
        :return: 假设最多可以翻转 k 个 0 ，则返回执行操作后 数组中连续 1 的最大个数
        """
        ans = 0
        left = 0
        cnt = Counter()
        for right, num in enumerate(nums):
            cnt[num] += 1

            while cnt[0] > k:
                cnt[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
