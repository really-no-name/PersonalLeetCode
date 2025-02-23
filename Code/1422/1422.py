#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 分割字符串的最大得分。
时间复杂度： O(N)
空间复杂度： O(1)
执行用时： 2 ms
消耗内存： 17.35 mb
"""


class Solution:
    def maxScore(self, s: str) -> int:
        left0 = 0
        right1 = s.count('1')
        ans = 0
        for i in s[:-1]:
            if i == '0':
                left0 += 1
            else:
                right1 -= 1
            ans = max(ans, left0 + right1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxScore("011101"))