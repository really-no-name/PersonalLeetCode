#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 两个数组间的距离值。
时间复杂度：
空间复杂度：
执行用时：
消耗内存：
"""
from typing import List


class Solution:
    def low_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        arr1.sort()
        arr2.sort()
        # print("list 1: ", arr1)
        # print("排序后的 list 2: ", arr2)

        for i in range(len(arr1)):
            index = self.low_bound(arr2, arr1[i])
            # print("大于等于 list 1 中: ", arr1[i], "的索引为", index)

            if index >= len(arr2):  # arr2 均小于 arr1[i]
                # print("Special 1")
                if arr1[i] - arr2[-1] > d:
                    # print("Special 1 is ok")
                    ans += 1
                break
            elif index == 0:  # arr2 均大于 arr1[i]\
                # print("Special 2")
                if arr2[0] - arr1[i] > d:
                    # print("Special 2 is ok")
                    ans += 1
                break

            # print("list 2 中索引为: ", index, " 的元素是: ", arr2[index])  # arr2[index] >= arr1[i]

            if arr2[index] != arr1[i]:
                # 确保 index - 1 是有效索引
                if index > 0 and abs(arr2[index - 1] - arr1[i]) > d and abs(arr2[index] - arr1[i]) > d:
                    # 满足条件时的逻辑
                    # print("Judgment 1")
                    # print("list 1: ", arr1[i], " is ok")
                    ans += 1
                elif index == 0 and abs(arr2[index] - arr1[i]) > d:
                    # 当 index 为 0 时，只需要检查 arr2[index] 和 arr1[i] 的差值
                    # print("Judgment 2")
                    # print("list 1: ", arr1[i], " is ok")
                    ans += 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    # print(sol.findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))
    # print(sol.findTheDistanceValue(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3))
    # print(sol.findTheDistanceValue(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6))
    # print(sol.findTheDistanceValue(arr1=[-3, 2, -5, 7, 1], arr2=[4], d=84))
    print(sol.findTheDistanceValue(arr1=[-3, -3, 4, -1, -10], arr2=[7, 10], d=12))
