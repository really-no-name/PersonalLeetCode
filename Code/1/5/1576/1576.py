#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1576.py
作者: Bolun Xu
创建日期: 2025/4/8
版本: 1.0
描述: 替换所有的问号。
时间复杂度： O(N∗M)
空间复杂度： O(N)
"""
import random


class Solution:
    def random_char_except(self, exclude_chars):
        while True:
            # 随机生成小写字母 (97~122)
            char = chr(random.randint(97, 122))
            if char not in exclude_chars:
                return char

    def modifyString(self, s: str) -> str:
        s_list = list(s)  # 转换为列表以便修改
        for i in range(len(s_list)):
            if s_list[i] == '?':
                # 确定需要排除的字符
                exclude = []
                if i > 0:
                    exclude.append(s_list[i-1])
                if i < len(s_list) - 1 and s_list[i+1] != '?':
                    exclude.append(s_list[i+1])
                # 获取随机字符
                s_list[i] = self.random_char_except(exclude)
        return ''.join(s_list)  # 转换回字符串