#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 球会落何处。
时间复杂度：O(M*N)
空间复杂度：O(N)
执行用时：3 ms
消耗内存：17.98 mb
"""
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ball_nums = len(grid[0])  # 球的数量，即网格的列数
        ans = [-1] * ball_nums  # 初始化结果数组，默认值为-1

        for i in range(ball_nums):  # 遍历每个球
            cur_col = i  # 当前球的初始列位置
            # print(f"开始处理第 {i} 个球，初始列位置: {cur_col}")

            for row_idx, row in enumerate(grid):  # 逐层处理网格
                direction = row[cur_col]  # 当前格子的方向（-1 或 1）
                next_col = cur_col + direction  # 计算下一个列位置

                # print(f"  第 {row_idx} 层，当前列: {cur_col}, 方向: {direction}, 下一个列: {next_col}")

                # 检查是否出界或形成V形
                if next_col < 0 or next_col >= ball_nums or row[next_col] != direction:
                    # print(f"    球 {i} 在第 {row_idx} 层被卡住，原因: ", end="")
                    # if next_col < 0:
                        # print("左边界出界")
                    # elif next_col >= ball_nums:
                        # print("右边界出界")
                    # else:
                        # print("形成V形结构")
                    cur_col = -1  # 标记为卡住
                    break

                cur_col = next_col  # 移动到下一个列

            # 如果所有层处理完毕且未被卡住，则更新结果
            if cur_col != -1:
                # print(f"球 {i} 成功到达底部，最终列位置: {cur_col}")
                ans[i] = cur_col
            # else:
                # print(f"球 {i} 未能到达底部，被卡住")

            # print()  # 分隔每个球的处理结果

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findBall(
        grid=[[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]))
