#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3340.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 检查平衡字符串。
时间复杂度： O(N)
空间复杂度： O(N)
"""


class Solution:
    def isBalanced(self, num: str) -> bool:
        num_list = list(num)
        print(f"DEBUG: {num_list}")
        sum_odd, sum_even = 0, 0
        for i, n in enumerate(num_list):
            if i % 2 == 0:  # 偶数
                sum_even += int(n)
            else:
                sum_odd += int(n)
        print(f"DEBUG: {sum_odd}, {sum_even}")
        return sum_odd == sum_even


if __name__ == "__main__":
    solution = Solution()
    print(solution.isBalanced("1234"))
