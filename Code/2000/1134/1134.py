#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1134.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 阿姆斯特朗数。
时间复杂度： O(K)
空间复杂度： O(K)
"""


class Solution:
    def isArmstrong(self, n: int) -> bool:
        """
        给你一个整数 n ，让你来判定他是否是 阿姆斯特朗数，是则返回 true，不是则返回 false。
        假设存在一个 k 位数 n ，其每一位上的数字的 k 次幂的总和也是 n ，那么这个数是阿姆斯特朗数 。
        """
        n_list = list(map(int, str(n)))
        k = len(n_list)
        armstrong = 0
        for number in n_list:
            armstrong += number ** k
        # print(f"DEBUG: {armstrong}")
        return armstrong == n


if __name__ == '__main__':
    sol = Solution()
    print(sol.isArmstrong(153))
    print(sol.isArmstrong(123))
