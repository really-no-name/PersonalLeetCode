#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1.py
作者: Bolun Xu
创建日期: 2025/4/12
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
from collections import deque, defaultdict
from typing import List


class Task:
    def __init__(self, id: int, duration: int, dependencies: List[int]):
        self.id = id
        self.duration = duration
        self.dependencies = dependencies if dependencies else []


def calculateMinTime(tasks: List[Task]) -> int:
    # Step 1: 构建图和入度信息
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    duration_map = {}

    for task in tasks:
        duration_map[task.id] = task.duration
        in_degree[task.id] = 0  # 初始化
    for task in tasks:
        for dep in task.dependencies:
            graph[dep].append(task.id)
            in_degree[task.id] += 1

    # Step 2: 拓扑排序初始化
    queue = deque()
    earliest_finish = defaultdict(int)

    for task in tasks:
        if in_degree[task.id] == 0:
            queue.append(task.id)
            earliest_finish[task.id] = duration_map[task.id]

    # Step 3: 拓扑排序 + 动态规划计算最早完成时间
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            earliest_finish[neighbor] = max(
                earliest_finish[neighbor],
                earliest_finish[curr] + duration_map[neighbor]
            )
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: 取最大完成时间
    return max(earliest_finish.values())


if __name__ == "__main__":
    n = int(input())
    tasks = []
    for _ in range(n):
        parts = list(map(int, input().split()))
        tid = parts[0]
        duration = parts[1]
        k = parts[2]
        deps = parts[3:] if k > 0 else []
        tasks.append(Task(tid, duration, deps))

    print(calculateMinTime(tasks))