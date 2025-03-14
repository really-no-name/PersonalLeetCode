#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1423.py
作者: Bolun Xu
创建日期: 2025/2/27
版本: 1.0
描述: 可获得的最大点数。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from math import inf
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        m = len(cardPoints) - k
        # print(m)
        ans = inf
        s = 0
        for i, card in enumerate(cardPoints):
            s += card
            if i < m - 1:
                continue
            ans = min(ans, s)
            s -= cardPoints[i - m + 1]
        return sum(cardPoints) - ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
    print(solution.maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7))
