#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2500.py
作者: Bolun Xu
创建日期: 2025/3/16
版本: 1.0
描述: 删除每行中的最大值。
时间复杂度： O(N ^ 2 Logn)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # 对每一行进行降序排序
        for line in grid:
            line.sort(reverse=True)

        # 打印排序后的 grid
        # print("排序后的 grid:")
        # for row in grid:
        #     print(row)
        #
        # # 打印解包后的 grid（*grid）
        # print("\n解包后的 grid (*grid):")
        # print(*grid)
        #
        # # 打印 zip(*grid) 的内容
        # print("\nzip(*grid) 的内容:")
        # print(list(zip(*grid)))
        #
        # # 打印 map(max, zip(*grid)) 的内容
        # print("\nmap(max, zip(*grid)) 的内容:")
        # print(list(map(max, zip(*grid))))

        # 计算每列的最大值并求和
        ans = sum(map(max, zip(*grid)))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))
