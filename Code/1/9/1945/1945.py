#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1945.py
作者: Bolun Xu
创建日期: 2025/4/7
版本: 1.0
描述: 字符串转化后的各位数字之和。
时间复杂度： O(N∗K)
空间复杂度： O(N)
"""


class Solution:
    def digit_sum(self, n: int) -> int:
        """
        计算数位和
        """
        # 将整数转换为字符串，以便逐个访问每个数字
        num_str = str(n)

        # 初始化总和为0
        total = 0

        # 遍历字符串中的每个字符
        for char in num_str:
            # 将字符转换回整数并加到总和中
            total += int(char)

        # 返回数位和
        return total

    def getLucky(self, s: str, k: int) -> int:
        s2num = ''
        for char in s:
            s2num += str(ord(char) - 96)
        print(s2num)

        while True:
            if k > 0:
                s2num = self.digit_sum(s2num)
                k -= 1
                print(s2num)
            else:
                break
        return s2num


if __name__ == '__main__':
    sol = Solution()
    print(sol.getLucky(s = "leetcode", k = 2))