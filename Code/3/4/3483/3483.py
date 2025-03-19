#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3483.py
作者: Bolun Xu
创建日期: 2025/3/19
版本: 1.0 -- 暴力循环
描述: 不同三位偶数的数目。
时间复杂度： O(N^3)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        st = set()  # 防止重复
        for i, a in enumerate(digits):  # 个位数
            if a % 2:  # 挑选偶数
                continue
            for j, b in enumerate(digits):  # 十位数
                if j == i:  # 排除个位数
                    continue
                for k, c in enumerate(digits):  # 百位数
                    if c == 0 or k == i or k == j:  # 排除前导0，个位数和十位数
                        continue
                    st.add(c * 100 + b * 10 + a)
        # print(f"DEBUG: st = {st}")
        return len(st)


if __name__ == "__main__":
    sol = Solution()
    print(sol.totalNumbers([1, 2, 3, 4]))
