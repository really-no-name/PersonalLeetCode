#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1802.py
作者: Bolun Xu
创建日期: 2025/3/28
版本: 1.0
描述: 有界数组中指定下标处的最大值。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def mountainListSum(self, top: int, index: int, length: int) -> int:
        """
        :param top: 峰值
        :param index: 峰值位置
        :param length: 山峰数组长度
        :return: 返回相邻差最大为1的山峰数组的和
        """

        if length == 1:
            return top
        # 计算左侧 共 index 个元素
        if top > index:  # 这 index 个元素构成等差数列，使用等差数列求和公式
            # 首项 top - index, 末项 index - 1
            left = index * (top - index + top - 1) // 2
        else:  # 后 top - 1 个元素构成等差数列，前面有 index - top + 1 个 1
            left = index - top + 1 + (1 + top - 1) * (top - 1) // 2

        right_index = length - index - 1
        if top > right_index:
            right = right_index * (top - right_index + top - 1) // 2
        else:
            right = right_index - top + 1 + (1 + top - 1) * (top - 1) // 2
        # # 左侧递增序列
        # left_length = index
        # left_start = max(1, top - left_length)
        # left_sum = (left_start + top - 1) * left_length // 2
        #
        # # 右侧递减序列
        # right_length = length - index - 1
        # right_end = max(1, top - right_length)
        # right_sum = (top - 1 + right_end) * right_length // 2

        print(left + top + right)
        return left + top + right

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = 0
        right = maxSum + 1
        while left + 1 < right:
            mid = (left + right) // 2
            print(left, mid, right)
            if self.mountainListSum(mid, index, n) <= maxSum:
                left = mid
            else:
                right = mid
        return left


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxValue(n=3, index=2, maxSum=18))
