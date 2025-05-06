#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1128.py
作者: Bolun Xu
创建日期: 2025/5/4
版本: 1.0
描述: 等价多米诺骨牌对的数量。
时间复杂度： O(N∗Log(N))
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        d = dict()
        for d1, d2 in dominoes:
            # 排序后加入字典
            index = tuple(sorted((d1, d2)))
            if index in d:
                d[index] += 1
            else:
                d[index] = 1
        # 计算答案
        for i in d:
            ans += d[i] * (d[i] - 1) // 2
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))