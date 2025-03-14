#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 完成旅途的最少时间 —— 递归写法。
时间复杂度：
空间复杂度：
执行用时：
消耗内存：
"""
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def dfs(t, bustotal):
            # 计算当前时间 t 下每辆公交车的运行趟数
            for i in range(len(bustotal)):
                bustotal[i] = t // time[i]
            # print(f"Debug: At time {t}, the buses run {bustotal}")

            # 计算总趟数
            total = sum(bustotal)

            # 如果总趟数大于等于目标趟数，返回当前时间 t
            if total >= totalTrips:
                return t
            # 否则，继续递归，时间加 1
            else:
                return dfs(t + 1, bustotal)

        # 初始化 bustotal 数组
        bustotal = [0] * len(time)
        # 从时间 t = 1 开始递归
        return dfs(1, bustotal)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTime([1, 2, 3], 5))
    print(sol.minimumTime([5, 10, 10], 9))
