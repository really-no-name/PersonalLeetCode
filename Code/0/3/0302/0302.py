#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0302.py
作者: Bolun Xu
创建日期: 2025/3/17
版本: 1.0 -- 暴力循环求解
描述: 包含全部黑色像素的最小矩形。
时间复杂度： O(N*M)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0  # 如果图像为空，返回 None

        rows = len(image)
        cols = len(image[0])

        # 初始化变量
        top = rows
        bottom = -1
        left = cols
        right = -1

        # 遍历每一行
        for i in range(rows):
            # 遍历每一列
            for j in range(cols):
                if image[i][j] == '1':
                    # 更新最上面和最下面的行
                    top = min(top, i)
                    bottom = max(bottom, i)
                    # 更新最左和最右的列
                    left = min(left, j)
                    right = max(right, j)

        # 如果没有找到 1，返回 None
        if top == rows:
            return 0
        print(top, bottom, left, right)
        return (bottom - top + 1) * (right - left + 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minArea(image=[["0", "0", "1", "0"], ["0", "1", "1", "0"], ["0", "1", "0", "0"]], x=0, y=2))
