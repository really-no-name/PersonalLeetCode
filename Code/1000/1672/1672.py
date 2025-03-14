#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 1672。
时间复杂度： O(N)
空间复杂度： O(N)
执行用时： 0 ms
消耗内存： 17.6 mb
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        account_sum = []
        for account in accounts:
            account_sum.append(sum(account))
        return max(account_sum)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]))
