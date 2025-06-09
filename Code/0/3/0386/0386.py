#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0386.py
作者: Bolun Xu
创建日期: 2025/6/9
版本: 1.0
描述: 字典序排数。
时间复杂度： O(NLogN)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # 创建一个包含 1 到 n 的整数列表
        nums = list(range(1, n + 1))
        # 使用字符串排序规则进行排序
        nums.sort(key=lambda x: str(x))
        return nums


if __name__ == '__main__':
    sol = Solution()
    print(sol.lexicalOrder(13))