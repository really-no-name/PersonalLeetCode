#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 将每个元素替换为右侧最大元素 —— 暴力求解。
时间复杂度：O(N)
空间复杂度：O(N)
执行用时：44 ms
消耗内存：18.83 mb
"""
from typing import List

# 暴力求解
# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         ans = [-1] * len(arr)
#         for i in range(len(arr) - 1):
#             ans[i] = max(arr[i + 1:])
#
#         return ans

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = -1
        ans = [-1] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            x = arr[i]
            ans[i] = max_value
            max_value = max(max_value, x)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceElements(arr=[17, 18, 5, 4, 6, 1]))
    print(sol.replaceElements(arr=[400]))
