#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 用地毯覆盖后的最少白色砖块。
时间复杂度： O(2^N)
空间复杂度： O(N)
执行用时： 1385 ms
消耗内存： 199.65 mb
"""

from functools import cache


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        # 将地板字符串转换为整数列表，方便后续处理
        floor = list(map(int, floor))  # 避免在 dfs 中频繁调用 int()

        @cache  # 使用缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def dfs(carpet_used: int, current_pos: int) -> int:
            """
            递归函数，计算在当前位置使用或不使用地毯时的最小白砖数。

            :param carpet_used: 已经使用的地毯数量
            :param current_pos: 当前处理的地板位置
            :return: 当前位置及之后的最小白砖数
            """
            # 如果剩余的地板可以被全部覆盖，则返回0（无需再计算）
            if current_pos < carpetLen * carpet_used:
                return 0

            # 如果没有地毯可用，则返回当前位置及之前的所有白砖数
            if carpet_used == 0:
                return dfs(carpet_used, current_pos - 1) + floor[current_pos]

            # 选择1：不使用地毯，保留当前白砖，继续递归
            option1 = dfs(carpet_used, current_pos - 1) + floor[current_pos]

            # 选择2：使用地毯，覆盖从 current_pos - carpetLen + 1 到 current_pos 的地板
            option2 = dfs(carpet_used - 1, current_pos - carpetLen)

            # 返回两种选择中的最小值
            return min(option1, option2)

        # 调用递归函数，从最后一个位置开始计算
        result = dfs(numCarpets, len(floor) - 1)

        # # 打印调试信息
        # print(f"Debug: Minimum white tiles remaining: {result}")

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumWhiteTiles(floor="10110101", numCarpets=2, carpetLen=2))
