#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 赎金信。
时间复杂度： O(N∗M)
空间复杂度： O(1)

"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            # print(c)
            if c not in magazine:
                return False
            else:
                magazine = magazine.replace(c, '', 1)
                # print(magazine)
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canConstruct("aa", "ab"))
