#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2712.py
作者: Bolun Xu
创建日期: 2025/3/27
版本: 1.0
描述: 使所有字符相等的最小成本。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def minimumCost(self, s: str) -> int:
        """
        相邻两个数是否相等不受共同翻转影响，因此若让相邻两数相同，需对其中之一进行翻转
        相邻两个数若不同，则翻转前缀或后缀，选择成本小的进行操作
        """
        n = len(s)
        ans = 0
        for i in range(1, n):
            print(f"DEBUG: 对于 {s[i]}")
            if s[i - 1] != s[i]:
                print(f"DEBUG: 翻转成本为 {min(i, n - i)}")
                ans += min(i, n - i)

            else:
                print(f"DEBUG: 无需翻转")
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumCost(s="010101"))
