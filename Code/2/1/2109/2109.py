#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2109.py
作者: Bolun Xu
创建日期: 2025/3/30
版本: 1.0
描述: 向字符串添加空格。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # s_list = list(s)
        # for i in range(len(spaces) - 1, -1, -1):
        #     print(f"DEBUG: {spaces[i]}")
        #     s_list.insert(spaces[i], " ")  # 在 pos 位置插入 char
        #     print(f"DEBUG: {s_list}")
        # new_s = "".join(s_list)  # 重新合并成字符串
        # return new_s
        result = []
        space_ptr = 0
        n = len(spaces)
        for i, char in enumerate(s):
            if space_ptr < n and i == spaces[space_ptr]:
                result.append(' ')
                space_ptr += 1
            result.append(char)
        return ''.join(result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))