#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2042.py
作者: Bolun Xu
创建日期: 2025/4/7
版本: 1.0
描述: 检查句子中的数字是否递增。
时间复杂度： O(N)
空间复杂度： O(N)
"""
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split()
        integers = [0]
        for token in tokens:
            try:
                num = int(token)
                if num > integers[-1]:
                    integers.append(num)
                    print(F"DEBUG: {integers}")
                else:
                    return False
            except ValueError:
                continue
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))