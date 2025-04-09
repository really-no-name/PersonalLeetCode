#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1816.py
作者: Bolun Xu
创建日期: 2025/4/9
版本: 1.0
描述: 截断句子。
时间复杂度： O(N)
空间复杂度： O(N)
"""
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans = s.split()  # 依据空格分割
        ans = ans[:k]
        ans = ' '.join(ans)  # 组合
        return ans