#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 这个文件用于演示Python文件模板的常用结构。
时间复杂度：
空间复杂度：
执行用时：
消耗内存：
"""
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                print("DEBUG: ", words[i])
                count += 1

        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.vowelStrings(words=["are", "amy", "u"], left=0, right=2))
    print(sol.vowelStrings(words=["hey", "aeo", "mu", "ooo", "artro"], left=1, right=4))
