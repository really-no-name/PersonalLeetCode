#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 设计相邻元素求和服务。
时间复杂度：
空间复杂度：
执行用时： 286 ms
消耗内存： 17.99 mb
"""
from typing import List


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        """
        初始化 neighborSum 类
        :param grid: 一个 n x n 的二维数组，包含不重复的元素
        """
        self.grid = grid
        self.n = len(grid)  # 获取 grid 的大小
        self.value_to_pos = {}  # 用于存储值到位置的映射

        # 遍历 grid, 构建值到位置的映射
        for i in range(self.n):
            for j in range(self.n):
                value = self.grid[i][j]
                self.value_to_pos[value] = (i, j)
                print(f"值 {value} 的位置是 （{i}, {j}）")

        print("值到位置的映射： ", self.value_to_pos)

    def adjacentSum(self, value: int) -> int:
        """
        计算与给定值相邻的元素之和
        相邻指的是上、下、左、右四个方向的元素
        :param value: 需要查询的值
        :return: 相邻元素的和
        """
        if value not in self.value_to_pos:
            print(f"值 {value} 不在 grid 中，返回 0")
            return 0

        # 获取值得位置
        i, j = self.value_to_pos[value]
        print(f"值 {value} 的位置是 （{i}, {j}）")

        # 定义四个方向
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total = 0

        # 遍历四个方向，计算和
        for di, dj in directions:
            ni, nj = i + di, j + dj  # 计算相邻位置的坐标
            if 0 <= ni < self.n and 0 <= nj < self.n:  # 检查是否在 grid 范围内
                neighbor_value = self.grid[ni][nj]
                total += neighbor_value
                print(f"相邻元素 {neighbor_value} 在位置 ({ni}, {nj})，当前总和为 {total}")
            else:
                print(f"位置 ({ni}, {nj}) 超出范围，忽略")

        print(f"值 {value} 的相邻元素之和为 {total}")
        return total

    def diagonalSum(self, value: int) -> int:
        """
                计算与给定值对角线相邻的元素之和。
                对角线相邻指的是左上、右上、左下、右下四个方向的元素。
                参数:
                    value: 需要查询的值。
                返回:
                    对角线相邻元素的和。
                """
        if value not in self.value_to_pos:
            print(f"值 {value} 不在 grid 中，返回 0")
            return 0

        # 获取值的位置
        i, j = self.value_to_pos[value]
        print(f"值 {value} 的位置是 ({i}, {j})")

        # 定义四个对角线方向：左上、右上、左下、右下
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        total = 0

        # 遍历四个方向，计算对角线相邻元素的和
        for di, dj in directions:
            ni, nj = i + di, j + dj  # 计算对角线位置的坐标
            if 0 <= ni < self.n and 0 <= nj < self.n:  # 检查是否在 grid 范围内
                neighbor_value = self.grid[ni][nj]
                total += neighbor_value
                print(f"对角线相邻元素 {neighbor_value} 在位置 ({ni}, {nj})，当前总和为 {total}")
            else:
                print(f"位置 ({ni}, {nj}) 超出范围，忽略")

        print(f"值 {value} 的对角线相邻元素之和为 {total}")
        return total


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)

if __name__ == "__main__":
    grid1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    neighborsum1 = NeighborSum(grid1)
    print("adjacentSum(1): ", neighborsum1.adjacentSum(1))
    print("adjacentSum(4): ", neighborsum1.adjacentSum(4))
    print("adjacentSum(4): ", neighborsum1.adjacentSum(4))
    print("adjacentSum(8): ", neighborsum1.adjacentSum(8))

