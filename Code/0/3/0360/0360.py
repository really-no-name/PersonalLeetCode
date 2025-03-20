#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0360.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 有序转化数组。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = []
        if a >= 0:  # 先存大的，从后向前
            while left < right:
                x = (nums[left] ** 2) * a + b * nums[left] + c
                y = (nums[right] ** 2) * a + b * nums[right] + c
                print(f"DEBUG: 当前左右指针的值{x} {y}")
                if x > y:
                    ans = [x] + ans
                    left += 1
                    print(f"DEBUG: 左指针加入{x}, {ans}")
                else:
                    ans = [y] + ans
                    right -= 1
                    print(f"DEBUG: 右指针加入{y}, {ans}")

            if left == right:
                ans = [(nums[left] ** 2) * a + b * nums[left] + c] + ans

        else:  # 先存小的，从前向后
            while left < right:
                x = (nums[left] ** 2) * a + b * nums[left] + c
                y = (nums[right] ** 2) * a + b * nums[right] + c
                print(f"DEBUG: 当前左右指针的值{x} {y}")
                if x > y:
                    ans = ans + [y]
                    right -= 1
                    print(f"DEBUG: 右指针加入{y}, {ans}")
                else:
                    ans = ans + [x]
                    left += 1
                    print(f"DEBUG: 左指针加入{x}, {ans}")
            if left == right:
                ans = ans + [(nums[left] ** 2) * a + b * nums[left] + c]
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortTransformedArray(nums=[-4, -2, 2, 4], a=1, b=3, c=5))
    print(sol.sortTransformedArray(nums=[-4, -2, 2, 4], a=-1, b=3, c=5))
