#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0658.py
作者: Bolun Xu
创建日期: 2025/3/4
版本: 1.0
描述: 找到 K 个最接近的元素。
时间复杂度： O(Log(N))
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        从数组中找到最靠近 x（两数之差最小）的 k 个数
        :param arr:  一个 排序好 的数组 arr
        :param k:
        :param x:
        :return:
        """
        left = 0
        right = len(arr) - 1
        while left < right:
            differ_left = abs(x - arr[left])
            print(f"DEBUG: 左侧边界 {arr[left]}, 差为 {differ_left}")
            differ_right = abs(x - arr[right])
            print(f"DEBUG: 右侧边界 {arr[right]}, 差为 {differ_right}")
            if right - left + 1 > k:
                if differ_left > differ_right:
                    left += 1
                    print(f"DEBUG: 左侧边界缩小")
                else:
                    right -= 1
                    print(f"DEBUG: 右侧边界缩小")
            else:
                break
        return arr[left:right + 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
    print(sol.findClosestElements(arr=[1, 1, 2, 3, 4, 5], k=4, x=-1))
