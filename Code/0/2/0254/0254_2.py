#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 因子的组合。
时间复杂度： O(N*Sqrt(N))
空间复杂度： O(N)
执行用时： 16 ms
消耗内存： 17.95 mb
"""
import math
from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        """
        返回整数 n 的所有因子组合
        :param n: 输入的整数
        :return: 所有因子组合的列表
        """

        def backtrack(target: int, start: int, path: List[int], result: List[List[int]], depth: int) -> None:
            """
            递归回溯函数，用于生成所有因子组合
            :param target: 当前需要分解的目标数
            :param start: 当前因子的起始值
            :param path: 当前路径
            :param result: 结果集
            """
            # 打印调试信息
            # indent = "  " * depth  # 根据递归深度缩进
            # print(f"Debug: {indent}-> backtrack(target={target}, start={start}, path={path})")

            # 如果目标数已经分解到1，且路径不为空，则将当前路径加入结果集
            if target == 1:
                if len(path) > 1:  # 避免将 n 本身作为因子
                    result.append(path[:])
                    # print(f"Debug: {indent} Found valid combination: {path}")
                # else:
                    # print(f"Debug: {indent} Invalid combination (path too short): {path}")
                return

            # 从 start 开始尝试分解 target
            for i in range(start, int(math.sqrt(target)) + 1):
                if target % i == 0:  # 如果 i 是 targe 的因子
                    path.append(i)  # 将 i 加入当前路径
                    # print(f"Debug: {indent} Trying factor {i}, new target: {target // i}")
                    backtrack(target // i, i, path, result, depth + 1)  # 递归分解 target // i
                    path.pop()  # 回溯，移除当前因子
                    # print(f"Debug: {indent} Backtracked, path is now: {path}")

            # 处理 target 本身作为因子的情况（例如，target 是质数）
            if target >= start and len(path) > 0:  # 避免将 n 本身作为因子
                path.append(target)
                result.append(path[:])
                path.pop()

        result = []
        backtrack(n, 2, [], result, 0)  # 从因子2 开始分解
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.getFactors(1))
    print(sol.getFactors(32))
