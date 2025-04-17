#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2243.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 计算字符串的数字和。
时间复杂度： O(Nlogn)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def dfs(s: str, k: int) -> str:
            if len(s) <= k:
                return s
            s = list(map(int, s))
            print(s)
            ans = []
            for i in range(0, len(s), k):
                if len(s) - i <= k:
                    print(s[i:])
                    ans.append(sum(s[i:]))
                else:
                    print(s[i:i + k])
                    ans.append(sum(s[i:i + k]))
            print(ans)
            ans = str(''.join(map(str, ans)))
            print(ans)
            return dfs(ans, k)

        return dfs(s, k)


if __name__ == '__main__':
    sol = Solution()
    print(sol.digitSum(s = "01234567890", k = 2))