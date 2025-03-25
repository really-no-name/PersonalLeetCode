#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2711.py
作者: Bolun Xu
创建日期: 2025/3/25
版本: 1.0 -- 暴力求解
描述: 对角线上不同值的数量差。
时间复杂度： O(M∗N)
空间复杂度： O(M+N)
"""
from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        st = set()
        for i in range(m):
            for j in range(n):
                print(f"DEBUG: 处理第 {i} 行 第 {j} 列 元素 {grid[i][j]}")

                # 计算 top_left[i][j]
                st.clear()
                x = i - 1
                y = j - 1
                while x >= 0 and y >= 0:
                    st.add(grid[x][y])
                    x -= 1
                    y -= 1
                top_left = len(st)
                print(f"DEBUG: top_left为 {top_left}")

                # 计算 bottomRight[i][j]
                st.clear()
                x = i + 1
                y = j + 1
                while x < m and y < n:
                    st.add(grid[x][y])
                    x += 1
                    y += 1
                bottom_right = len(st)
                print(f"DEBUG: bottom_right为 {bottom_right}")
                ans[i][j] = abs(bottom_right - top_left)
                print(f"DEBUG: 对应答案为 {ans[i][j]}")
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.differenceOfDistinctValues([[1, 2, 3], [3, 1, 5], [3, 2, 1]]))
