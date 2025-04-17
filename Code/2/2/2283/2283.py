#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2283.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 判断一个数的数字计数是否等于数位的值。
时间复杂度： O(N)
空间复杂度： O(K)
"""
from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        cnt = Counter(num)
        print(cnt)
        for i in range(len(num)):
            print(int(num[i]), cnt[str(i)])
            if int(num[i]) != cnt[str(i)]:
                return False
        return True
