#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1052.py
作者: Bolun Xu
创建日期: 2025/2/27
版本: 1.0
描述: 爱生气的书店老板。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        s = 0
        for i, customer in enumerate(customers):
            if grumpy[i] == 0:
                s += customer
        # print(s)

        for i, customer in enumerate(customers):
            # print(f"DEBUG: customer {customer} 进入窗口")
            if grumpy[i] != 0:
                s += customer  # 进入窗口的不满意 变 满意

            if i < minutes - 1:
                continue

            ans = max(ans, s)
            # print(f"DEBUG: 目前为 {ans} ")

            if grumpy[i - minutes + 1] != 0:
                s -= customers[i - minutes + 1]
        return ans


if __name__ == '__main__':
    sol = Solution()
    # print(sol.maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3))
    # print(sol.maxSatisfied(customers=[1], grumpy=[0], minutes=1))
    print(sol.maxSatisfied(customers=[4, 10, 10], grumpy=[1, 1, 0], minutes=2))
