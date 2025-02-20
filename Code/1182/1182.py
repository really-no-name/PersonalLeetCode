#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 与目标颜色间的最短距离。
时间复杂度： O(N∗Q∗Log(M))
空间复杂度： O(N)
执行用时： 187 ms
消耗内存： 34.05 mb
"""
import bisect
from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:  # 预处理：记录每种颜色的所有索引
        color_indices = {1: [], 2: [], 3: []}
        for idx, color in enumerate(colors):
            color_indices[color].append(idx)

        # print("Debug: 预处理结果：")
        # print("Debug: 颜色 1 的索引列表:", color_indices[1])
        # print("Debug: 颜色 2 的索引列表:", color_indices[2])
        # print("Debug: 颜色 3 的索引列表:", color_indices[3])
        # print()

        result = []
        for query_idx, (i, c) in enumerate(queries):
            # print(f"Debug: 处理查询 {query_idx + 1}: (i={i}, c={c})")

            # 检查颜色 c 是否存在
            if c not in color_indices or not color_indices[c]:
                # print(f"Debug: 颜色 {c} 不存在，返回 -1")
                result.append(-1)
                continue

            # 获取颜色 c 的所有索引
            indices = color_indices[c]
            # print(f"Debug: 颜色 {c} 的索引列表:", indices)

            # 使用 bisect 找到 i 应该插入的位置
            pos = bisect.bisect_left(indices, i)
            # print(f"Debug: 在索引列表中找到 i={i} 的插入位置: pos={pos}")

            # 检查 pos 和 pos-1 的位置
            candidates = []
            if pos < len(indices):
                distance = indices[pos] - i
                # print(f"Debug: 检查右侧索引 {indices[pos]}，距离为 {distance}")
                candidates.append(distance)
            if pos > 0:
                distance = i - indices[pos - 1]
                # print(f"Debug: 检查左侧索引 {indices[pos - 1]}，距离为 {distance}")
                candidates.append(distance)

            # 找到最小的距离
            if candidates:
                min_distance = min(candidates)
                # print(f"Debug: 最小距离为 {min_distance}")
                result.append(min_distance)
            else:
                # print("Debug: 没有找到有效的距离，返回 -1")
                result.append(-1)

            # print()

        return result


if __name__ == "__main__":
    sol = Solution()
    # 示例 1
    colors = [1, 1, 2, 1, 3, 2, 2, 3, 3]
    queries = [[1, 3], [2, 2], [6, 1]]
    print("示例 1 的查询结果:", sol.shortestDistanceColor(colors, queries))  # 输出: [3, 0, 3]

    # 示例 2
    colors = [1, 2]
    queries = [[0, 3]]
    print("示例 2 的查询结果:", sol.shortestDistanceColor(colors, queries))  # 输出: [-1]
