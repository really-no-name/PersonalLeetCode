#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3286.py
作者: Bolun Xu
创建日期: 2026/7/2
版本: 1.0
描述: 穿越网格图的安全路径
"""
from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # 如果起点本身就不安全，先扣除健康值
        initial_health = health - grid[0][0]
        # 起点就要保证健康值 > 0
        if initial_health <= 0:
            return False
        
        # visited[i][j][h] 表示在 (i,j) 位置，剩余健康值为 h 时是否访问过
        visited = [[[False] * (health + 1) for _ in range(n)] for _ in range(m)]
        
        # BFS队列，存储 (行, 列, 剩余健康值)
        q = deque()
        q.append((0, 0, initial_health))
        visited[0][0][initial_health] = True
        
        # 四个方向：上、下、左、右
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            x, y, cur_health = q.popleft()
            
            # 如果到达终点，且健康值为正（此处已经在加入队列时确保 >0，但以防万一再判断）
            if x == m - 1 and y == n - 1:
                return True
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                # 检查边界
                if 0 <= nx < m and 0 <= ny < n:
                    # 到达新格子需要的健康值
                    new_health = cur_health - grid[nx][ny]
                    # 健康值必须保持正数
                    if new_health > 0 and not visited[nx][ny][new_health]:
                        visited[nx][ny][new_health] = True
                        q.append((nx, ny, new_health))
        
        # 如果BFS结束还没找到，返回False
        return False
        


if __name__ == '__main__':
    sol = Solution()
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    health = 1
    print(sol.findSafeWalk(grid, health))