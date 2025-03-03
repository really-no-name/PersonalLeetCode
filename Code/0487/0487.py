#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0487.py
作者: Bolun Xu
创建日期: 2025/3/3
版本: 1.0
描述: 最大连续1的个数 II。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """

        :param nums: 二进制数组
        :return: 最多可以翻转一个 0 ，则返回数组中连续 1 的最大个数
        """
        ans = 0
        cnt = Counter()
        left = 0
        for right, num in enumerate(nums):
            cnt[num] += 1

            while cnt[0] > 1:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0]))
