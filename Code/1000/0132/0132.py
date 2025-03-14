#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0132.py
作者: Bolun Xu
创建日期: 2025/3/2
版本: 1.0
描述: 分割回文串 II。
时间复杂度： O(N^2)
空间复杂度： O(N^2)
"""
from functools import cache
from math import inf


class Solution:
    def minCut(self, s: str) -> int:
        # 返回 s[l:r+1] 是否为回文串
        @cache  # 缓存装饰器，避免重复计算 is_palindrome（一行代码实现记忆化）
        def is_palindrome(l: int, r: int) -> bool:
            # 如果左指针大于等于右指针，说明子串是回文串
            if l >= r:
                return True
            # 递归检查 s[l] 是否等于 s[r]，并且 s[l+1:r] 也是回文串
            return s[l] == s[r] and is_palindrome(l + 1, r - 1)

        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(r: int) -> int:
            # 如果 s[0:r+1] 已经是回文串，则不需要分割，返回 0
            if is_palindrome(0, r):
                return 0
            # 初始化结果为无穷大，用于后续取最小值
            res = inf
            # 枚举所有可能的分割位置 l
            for l in range(1, r + 1):
                # 如果 s[l:r+1] 是回文串，则尝试在 l-1 和 l 之间进行分割
                if is_palindrome(l, r):
                    # 更新结果为当前分割次数的最小值
                    res = min(res, dfs(l - 1) + 1)
            return res

        # 从字符串的最后一个字符开始进行深度优先搜索
        return dfs(len(s) - 1)


# 调试信息
# 可以通过打印语句来调试代码，例如：
# print(is_palindrome.cache_info())  # 查看 is_palindrome 函数的缓存信息
# print(dfs.cache_info())  # 查看 dfs 函数的缓存信息


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCut("aab"))  # 输出: 1
    print(solution.minCut("abcba"))  # 输出: 0
