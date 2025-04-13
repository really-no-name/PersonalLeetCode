#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1.py
作者: Bolun Xu
创建日期: 2025/4/12
版本: 1.0
描述: ok。
时间复杂度：
空间复杂度：
"""
from collections import deque


class Task:
    def __init__(self, id, duration, dependencies):
        self.id = id
        self.duration = duration
        self.dependencies = dependencies if dependencies is not None else []


def calculateMinTime(tasks):
    if not tasks:
        return 0

    # 创建任务字典，方便通过id访问
    task_dict = {task.id: task for task in tasks}
    n = len(tasks)

    # 构建邻接表和入度表
    adj = {task.id: [] for task in tasks}
    in_degree = {task.id: 0 for task in tasks}

    for task in tasks:
        for dep in task.dependencies:
            adj[dep].append(task.id)
            in_degree[task.id] += 1

    # 拓扑排序检测环并初始化队列
    queue = deque()
    for task in tasks:
        if in_degree[task.id] == 0:
            queue.append(task.id)

    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # 如果拓扑排序结果不包含所有任务，说明有环
    if len(topo_order) != n:
        return -1

    # 计算每个任务的最早完成时间
    completion_time = {task.id: 0 for task in tasks}
    max_time = 0

    for u in topo_order:
        task = task_dict[u]
        max_dep_time = 0
        for dep in task.dependencies:
            if completion_time[dep] > max_dep_time:
                max_dep_time = completion_time[dep]
        completion_time[u] = max_dep_time + task.duration
        if completion_time[u] > max_time:
            max_time = completion_time[u]

    return max_time


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