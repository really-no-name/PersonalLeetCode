#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1733.py
作者: Bolun Xu
创建日期: 2025/9/10
版本: 1.0
描述: 需要教语言的最少人数。
时间复杂度：
空间复杂度：
"""
from math import inf
from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        learned = list(map(set, languages))

        todo_list = []
        for u, v in friendships:
            # u 和 v 减一，下标从 0 开始
            if learned[u - 1].isdisjoint(learned[v - 1]):  # 无交集
                todo_list.append((u - 1, v - 1))

        ans = inf
        for k in range(1, n + 1):  # 枚举需要教的语言 k
            st = set()
            for u, v in todo_list:
                if k not in learned[u]:  # u 需要学习语言 k
                    st.add(u)
                if k not in learned[v]:  # v 需要学习语言 k
                    st.add(v)
            ans = min(ans, len(st))  # len(st) 是需要学习语言 k 的人数
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTeachings(n=2, languages=[[1], [2], [1, 2]], friendships=[[1, 2], [1, 3], [2, 3]]))
