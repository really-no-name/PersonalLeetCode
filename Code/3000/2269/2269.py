#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2269.py
作者: Bolun Xu
创建日期: 2025/3/11
版本: 1.0
描述: 找到一个数字的 K 美丽值。
时间复杂度：
空间复杂度：
"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        print(f"DEBUG: {s}")
        ans = 0
        for i in range(k, len(s) + 1):
            x = int(s[i - k: i])  # 长为 k 的子串
            print(f"DEBUG: {x}")
            if x > 0 and num % x == 0:  # 子串能整除 num
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.divisorSubstrings(num=240, k=2))
