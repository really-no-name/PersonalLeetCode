#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1859.py
作者: Bolun Xu
创建日期: 2025/4/10
版本: 1.0
描述: 将句子排序。
时间复杂度： O(N)
空间复杂度： O(N)
"""
class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split()
        print(s_list)
        ans = [''] * len(s_list)
        for word in s_list:
            print(int(word[-1]))
            print(word[:-1])
            ans[int(word[-1]) - 1] = word[:-1]
        return ' '.join(ans)