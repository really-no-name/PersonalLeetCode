#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1528.py
作者: Bolun Xu
创建日期: 2025/4/2
版本: 1.0
描述: 重新排列字符串。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [''] * len(s)
        for i, indice in enumerate(indices):
            ans[indice] = s[i]
        return ''.join(ans)


if __name__ == '__main__':
    sol = Solution()
    print(sol.restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))
