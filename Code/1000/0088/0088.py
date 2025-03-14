#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 合并两个有序数组。
时间复杂度： O((M+N)Log(M+N))
空间复杂度： O(1)

"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        # print(f"DEBUG: nums1 = {nums1}")
        del nums2[n:]
        # print(f"DEBUG: nums2 = {nums2}")
        nums1.extend(nums2)
        # print(f"DEBUG: nums1 = {nums1}")
        nums1.sort()


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1, m=3, nums2=[2, 5, 6], n=3)
    print(nums1)
