#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 寻找两个正序数组的中位数 —— 双指针。
时间复杂度： O(N)
空间复杂度： O(N)
执行用时： 11 ms
消耗内存： 18.07 mb
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0  # 初始化两个指针
        sum_list = []
        total_len = len(nums1) + len(nums2)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum_list.append(nums1[i])
                i += 1
            else:
                sum_list.append(nums2[j])
                j += 1

        while i < len(nums1):
            sum_list.append(nums1[i])
            i += 1
        while j < len(nums2):
            sum_list.append(nums2[j])
            j += 1
        # print(sum_list)

        if total_len % 2 == 0:  # 双数
            median = (sum_list[total_len // 2 - 1] + sum_list[total_len // 2]) / 2
        else:  # 单数
            median = sum_list[(total_len - 1) // 2]
        return median


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
    print(sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
