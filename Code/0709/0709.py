#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 转换成小写字母。
时间复杂度： O(N)
空间复杂度： O(1)
执行用时： 0 ms
消耗内存： 17.38 mb
"""
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


if __name__ == '__main__':
    solution = Solution()
    print(solution.toLowerCase('Hello'))
