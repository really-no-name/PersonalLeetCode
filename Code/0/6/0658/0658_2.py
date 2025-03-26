#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0658.py
作者: Bolun Xu
创建日期: 2025/3/4
版本: 1.0 -- 二分查找
描述: 找到 K 个最接近的元素。
时间复杂度： O(Log(N))
空间复杂度： O(1)
"""
import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        从数组中找到最靠近 x（两数之差最小）的 k 个数
        :param arr:  一个 排序好 的数组 arr
        """
        if x <= arr[0]:
            return arr[0:k]
        elif x >= arr[-1]:
            return arr[-k:]

        size = len(arr)
        left = 0
        right = size - k
        print(f"DEBUG: 初始化left={left}({arr[left]}), right={right}({arr[right]})")

        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) // 2
            # 尝试从长度为 k + 1 的连续子区间删除一个元素
            # 从而定位左区间端点的边界值
            if x - arr[mid] > arr[mid + k] - x:  # 左侧 差 大于 右侧 差
                # 下一轮搜索区间是 [mid + 1..right]
                left = mid + 1
            else:
                # 下一轮搜索区间是 [left..mid]
                right = mid
        return arr[left:left + k]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
    print(sol.findClosestElements(arr=[1, 1, 2, 3, 4, 5], k=4, x=-1))
