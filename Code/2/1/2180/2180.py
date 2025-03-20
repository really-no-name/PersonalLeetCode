#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2180.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 统计各位数字之和为偶数的整数个数。
时间复杂度： O(N ^ 2 )
空间复杂度： O(1)
"""


class Solution:
    def digit_sum(self, n):
        # 将整数转换为字符串，方便逐位处理
        n_str = str(n)
        # 初始化总和为0
        total = 0
        # 遍历字符串中的每个字符
        for char in n_str:
            # 将字符转换回整数并加到总和中
            total += int(char)
        # 返回总和
        return total

    def countEven(self, num: int) -> int:
        ans = 0
        while num > 1:
            if self.digit_sum(num) % 2 == 0:
                ans += 1
            num -= 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countEven(4))