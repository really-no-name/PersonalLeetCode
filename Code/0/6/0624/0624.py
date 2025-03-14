#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 这个文件用于演示Python文件模板的常用结构。
时间复杂度：
空间复杂度：
执行用时：
消耗内存：
"""
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # 初始化最小值和最大值
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0

        # print(f"初始值: min_val = {min_val}, max_val = {max_val}, max_distance = {max_distance}")

        # 遍历所有数组
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            # print(f"\n处理第 {i} 个数组: current_min = {current_min}, current_max = {current_max}")

            # 计算当前数组的最小值和最大值与之前的最小值和最大值的距离
            distance1 = abs(current_max - min_val)
            distance2 = abs(max_val - current_min)

            # print(
            #         f"计算距离: distance1 = {distance1} (current_max - min_val), distance2 = {distance2} (max_val - current_min)")

            # 更新最大距离
            max_distance = max(max_distance, distance1, distance2)

            # print(f"更新后的 max_distance = {max_distance}")

            # 更新全局最小值和最大值
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

            # print(f"更新后的 min_val = {min_val}, max_val = {max_val}")

        return max_distance


if __name__ == "__main__":
    sol = Solution()
    # 示例 1
    arrays1 = [[1, 2, 3], [4, 5], [1, 2, 3]]
    print("示例 1 结果:", sol.maxDistance(arrays1))  # 输出: 4

    # 示例 2
    arrays2 = [[1], [1]]
    print("示例 2 结果:", sol.maxDistance(arrays2))  # 输出: 0