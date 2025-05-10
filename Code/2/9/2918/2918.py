#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2918.py
作者: Bolun Xu
创建日期: 2025/5/10
版本: 1.0
描述: 数组的最小相等和。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from collections import Counter
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(max(x, 1) for x in nums1)
        sum2 = sum(max(x, 1) for x in nums2)
        if sum1 < sum2 and 0 not in nums1 or \
                sum2 < sum1 and 0 not in nums2:
            return -1
        return max(sum1, sum2)


if __name__ == '__main__':
    sol = Solution()
    print('Test 1\n', sol.minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0]))
    print('Test 2\n', sol.minSum(nums1 = [2,0,2,0], nums2 = [1,4]))
    print('Test 3\n', sol.minSum(nums1=[0,17,20,17,5,0,14,19,7,8,16,18,6], nums2=[21,1,27,19,2,2,24,21,16,1,13,27,8,5,3,11,13,7,29,7]))
