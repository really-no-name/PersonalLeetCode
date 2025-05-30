#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2359.py
作者: Bolun Xu
创建日期: 2025/5/30
版本: 1.0
描述: 找到离给定两个节点最近的节点。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import deque
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def bfs(start):
            dist = [-1] * n
            q = deque()
            q.append(start)
            dist[start] = 0
            while q:
                node = q.popleft()
                neighbor = edges[node]
                if neighbor != -1 and dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)
            return dist

        dist1 = bfs(node1)
        dist2 = bfs(node2)

        min_max_dist = float('inf')
        result_node = -1

        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                current_max = max(dist1[i], dist2[i])
                if current_max < min_max_dist:
                    min_max_dist = current_max
                    result_node = i
                elif current_max == min_max_dist:
                    if i < result_node:
                        result_node = i
        return result_node


if __name__ == '__main__':
    sol = Solution()
    print(sol.closestMeetingNode(edges=[2, 2, 3, -1], node1=0, node2=1))
