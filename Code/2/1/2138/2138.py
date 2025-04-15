#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2138.py
作者: Bolun Xu
创建日期: 2025/4/15
版本: 1.0
描述: 将字符串拆分为若干长度为 k 的组。
时间复杂度： O(Nk)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s) % k != 0:
            n = k - len(s) % k
            s = s + fill * n
        print(s)
        ans = []
        for i in range(0, len(s), k):
            ans.append(s[i: i + k])
        return ans