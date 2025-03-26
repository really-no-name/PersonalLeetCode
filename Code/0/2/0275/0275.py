#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0275.py
作者: Bolun Xu
创建日期: 2025/3/26
版本: 1.0
描述: H 指数 II。
时间复杂度： O(Nlogn)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n

        print(f"排序后的引用次数: {citations}")
        print(f"初始搜索范围: left={left}, right={right}\n")

        while left <= right:
            mid = (left + right) // 2
            print(f"\n--- 当前循环 ---")
            print(f"当前搜索范围: [{left}, {right}]")
            print(f"计算中点: mid = ({left} + {right}) // 2 = {mid}")

            # 检查第n-mid篇论文的引用次数是否>=mid
            if mid == 0:
                check_index = -1  # 特殊情况处理
                check_value = float('inf')  # 视为极大值
            else:
                check_index = -mid
                check_value = citations[-mid]

            print(f"检查条件: citations[{check_index}] >= {mid} ? ({check_value} >= {mid})")

            if check_value >= mid:
                print(f"满足条件: 至少有{mid}篇论文被引用至少{mid}次")
                print(f"尝试更大的h指数: 移动left从{left}到{mid + 1}")
                left = mid + 1
            else:
                print(f"不满足条件: 不足{mid}篇论文被引用至少{mid}次")
                print(f"尝试更小的h指数: 移动right从{right}到{mid - 1}")
                right = mid - 1

            print(f"更新后搜索范围: [{left}, {right}]")

        print("\n--- 循环结束 ---")
        print(f"最终结果: right={right} (left={left}, right=left-1)")
        print(f"最大h指数: {right}")
        return right


if __name__ == '__main__':
    sol = Solution()
    print(sol.hIndex([0, 1, 3, 5, 6]))
