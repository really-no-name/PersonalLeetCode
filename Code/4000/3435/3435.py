#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3435.py
作者: Bolun Xu
创建日期: 2025/3/6
版本: 1.0
描述: 分割正方形 I。
时间复杂度： O((Log(MAXY*M)) * N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # 定义一个较大的常数 M，用于控制二分查找的精度
        M = 100_000

        # 计算所有正方形的总面积
        total_area = sum(l * l for _, _, l in squares)
        # print(f"Total area of all squares: {total_area}")

        # 定义一个内部函数 check，用于检查在 y 坐标处是否满足条件
        def check(y: float) -> bool:
            area = 0
            for _, yi, l in squares:
                # 如果正方形的 y 坐标小于 y，则计算该正方形在 y 以下的面积
                if yi < y:
                    # 计算正方形在 y 以下的面积：取 min(y - yi, l) * l
                    area += l * min(y - yi, l)
            # print(f"Checking y = {y}, accumulated area = {area}, required area = {total_area / 2}")
            # 返回是否满足条件：累计面积是否大于等于总面积的一半
            return area >= total_area / 2

        # 初始化二分查找的左右边界
        left = 0
        right = max_y = max(y + l for _, y, l in squares)
        # print(f"Initial left: {left}, right: {right}, max_y: {max_y}")

        # 进行二分查找，迭代次数为 max_y * M 的二进制位数
        for i in range((max_y * M).bit_length()):
            mid = (left + right) / 2
            # print(f"Iteration {i + 1}: mid = {mid}, left = {left}, right = {right}")
            if check(mid):
                # 如果 mid 满足条件，则将右边界移动到 mid
                right = mid
            else:
                # 否则将左边界移动到 mid
                left = mid

        # 返回最终的中点作为结果，误差较小
        result = (left + right) / 2
        # print(f"Final result: {result}")
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.separateSquares(squares=[[0, 0, 1], [2, 2, 1]]))  # 输出：1.00000
    print(solution.separateSquares(squares=[[0, 0, 2], [1, 1, 1]]))  # 输出：1.16667
