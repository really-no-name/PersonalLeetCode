#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1652.py
作者: Bolun Xu
创建日期: 2025/2/27
版本: 1.0
描述: 拆炸弹 -- 基础解法。
时间复杂度： O(Nk)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l = len(code)
        if k == 0:
            return [0] * len(code)
        if k > 0:
            code += code[:k]
            # print(f"DEBUG: {code}")
            ans = [0] * l
            for i in range(l):
                # 计算 code[i]
                ans[i] = sum(code[i + 1:i + k + 1])
                # print(f"DEBUG: {code[i]} --> {ans[i]} ")
        else:
            code = code[k:] + code
            # print(f"DEBUG: {code}")
            ans = [0] * l
            for i in range(l):
                # 计算 code[i + start]
                ans[i] = sum(code[i:i - k])
                # print(f"DEBUG: {code[i + start]} --> {ans[i]} ")

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.decrypt(code=[5, 7, 1, 4], k=3))
    print(sol.decrypt(code=[1, 2, 3, 4], k=0))
    print(sol.decrypt(code=[2, 4, 9, 3], k=-2))
