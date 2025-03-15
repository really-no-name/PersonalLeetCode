#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2107.py
作者: Bolun Xu
创建日期: 2025/3/1
版本: 1.0
描述: 分享 K 个糖果后独特口味的数量。
时间复杂度：
空间复杂度：
"""
from collections import defaultdict
from typing import List


class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        if k == 0:
            return len(candies)
        # 初始化统计所有糖果的出现次数
        total_count = defaultdict(int)
        for candie in candies:
            total_count[candie] += 1

        # 统计所有不同糖果的数量
        distinct_total = len(total_count)
        # 初始化窗口外不同糖果的数量
        distinct_out = distinct_total
        # 记录窗口中每个糖果的出现次数
        window_count = defaultdict(int)

        ans = 0

        for i, candie in enumerate(candies):
            print("-----------------------------------------------------------------------")
            print(f"DEBUG: 处理第 {i} 个元素: {candie}")

            # 元素进入窗口，减少其在 total_count 中的计数
            total_count[candie] -= 1
            print(f"DEBUG: 糖果 {candie} 进入窗口，剩余次数: {total_count[candie]}")

            # 如果 total_count[candie] 变为 0，说明窗口外不再有这个糖果
            if total_count[candie] == 0:
                distinct_out -= 1
                print(f"DEBUG: 糖果 {candie} 在窗口外消失，窗口外不同糖果数量: {distinct_out}")

            # 更新窗口内糖果的计数
            window_count[candie] += 1
            print(f"DEBUG: 窗口内糖果 {candie} 的出现次数增加到: {window_count[candie]}")

            # 如果窗口大小达到 k，开始统计窗口外不同糖果的数量
            if i >= k - 1:
                ans = max(ans, distinct_out)
                print(f"DEBUG: 窗口大小达到 {k}，当前窗口外不同糖果数量: {distinct_out}")

                # 窗口最左边的元素离开窗口
                left_candie = candies[i - k + 1]
                window_count[left_candie] -= 1
                print(f"DEBUG: 糖果 {left_candie} 离开窗口，窗口内剩余次数: {window_count[left_candie]}")

                # 如果窗口内不再有这个糖果，增加其在 total_count 中的计数
                if window_count[left_candie] == 0:
                    total_count[left_candie] += 1
                    print(f"DEBUG: 糖果 {left_candie} 在窗口内消失，剩余次数: {total_count[left_candie]}")

                    # 如果 total_count[left_candie] 从 0 变为 1，说明窗口外重新出现这个糖果
                    if total_count[left_candie] == 1:
                        distinct_out += 1
                        print(f"DEBUG: 糖果 {left_candie} 重新出现在窗口外，窗口外不同糖果数量: {distinct_out}")

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.shareCandies(candies=[1,2,3,2,2,2], k=3))
