#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2.py
作者: Bolun Xu
创建日期: 2025/4/12
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
from typing import List


class Solution:
    def maxCM(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))  # 开始会议 +1
            events.append((end, -1))   # 结束会议 -1

        # 按时间排序，若时间相同则结束事件优先
        events.sort(key=lambda x: (x[0], x[1]))

        max_meetings = 0
        current_meetings = 0

        for time, change in events:
            current_meetings += change
            max_meetings = max(max_meetings, current_meetings)

        return max_meetings

# 示例输入处理（可注释掉用于系统调用）
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    intervals = []
    for _ in range(n):
        start, end = map(int, input().split())
        intervals.append([start, end])

    print(sol.maxCM(intervals))