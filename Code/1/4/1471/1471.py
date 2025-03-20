#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1471.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 数组中的 k 个最强值。
时间复杂度： O(Nlogn)
空间复杂度： O(N)
"""
import math
from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        print(f"DEBUG: 中位数是 {m}")
        ans = []
        value_nus = 0
        left = 0
        right = len(arr) - 1
        while left < right:
            print(f"DEBUG: {arr[left]} {arr[right]}")
            if abs(arr[left] - m) > abs(arr[right] - m) or (
                    abs(arr[left] - m) == abs(arr[right] - m) and arr[left] > arr[right]):
                value_nus += 1
                ans.append(arr[left])
                print(f"DEBUG: 左指针对应的 {arr[left]} 更强， 加入ans {ans}")
                left += 1
            else:
                value_nus += 1
                ans.append(arr[right])
                print(f"DEBUG: 右指针对应的 {arr[right]} 更强， 加入ans {ans}")
                right -= 1
            if value_nus == k:
                return ans
        if left == right:
            ans.append(arr[left])
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.getStrongest(arr=[1, 2, 3, 4, 5], k=2))
    print(sol.getStrongest(arr=[1, 1, 3, 5, 5], k=2))
    print(sol.getStrongest(arr=[6, 7, 11, 7, 6, 8], k=5))
    print(sol.getStrongest(arr=[6, -3, 7, 2, 11], k=3))
