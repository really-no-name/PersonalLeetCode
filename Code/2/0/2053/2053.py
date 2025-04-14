#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2053.py
作者: Bolun Xu
创建日期: 2025/4/14
版本: 1.0
描述: 数组中第 K 个独一无二的字符串。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        ans = ''
        for i in arr:
            if cnt[i] == 1:
                k -= 1
                if k == 0:
                    ans = i
        return ans