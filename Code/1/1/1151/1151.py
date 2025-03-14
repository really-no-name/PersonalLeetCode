#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1151.py
作者: Bolun Xu
创建日期: 2025/3/1
版本: 1.0
描述: 最少交换次数来组合所有的 1。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        s = 0
        k = data.count(1)
        if k == 0:
            return 0
        ans = data.count(0)
        for i, val in enumerate(data):
            if val == 0:
                s += 1
            if i < k - 1:
                continue
            ans = min(ans, s)
            if data[i - k + 1] == 0:
                s -= 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSwaps(data=[1, 0, 1, 0, 1]))
