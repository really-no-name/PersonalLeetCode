#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2566.py
作者: Bolun Xu
创建日期: 2025/6/14
版本: 1.0
描述: 替换一个数字后的最大差值。
时间复杂度： O(N)
空间复杂度： O(1)
"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_num, min_num = num, 0
        for c in s:
            if c != '9':  # 第一个不等于 9 的字符
                max_num = int(s.replace(c, '9'))  # 替换成 9
                break
        min_num = int(s.replace(s[0], '0'))  # 第一个不等于 0 的字符，替换成 0
        return max_num - min_num


if __name__ == '__main__':
    sol = Solution()
    print(sol.minMaxDifference(90))