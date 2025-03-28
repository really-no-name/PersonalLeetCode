#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1898.py
作者: Bolun Xu
创建日期: 2025/3/28
版本: 1.0
描述: 可移除字符的最大数目。
时间复杂度： O(N∗M)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def check(self, s: str, p: str, removable: List[int], k: int) -> bool:
        # for rm in removable[:k]:
        #     s = s[:rm] + "!" + s[rm + 1:]
        # s = s.replace("!", "")
        # print(f"DEBUG: 移除了 {removable[:k]} 元素的字符串为 {s}")
        # it = iter(s)
        # return all(c in it for c in p)
        removed = set(removable[:k])
        it = (c for i, c in enumerate(s) if i not in removed)
        return all(c in it for c in p)

    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left = 0
        right = len(removable) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            print(f"DEBUG: {left}, {mid}, {right}")
            if self.check(s, p, removable, mid):
                print(f"DEBUG: 符合，右移")
                left = mid
            else:
                print(f"DEBUG: 不符合，左移")
                right = mid
        return left


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumRemovals(s = "qlevcvgzfpryiqlwy", p = "qlecfqlw", removable = [12,5]))
    print(solution.maximumRemovals(s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]))
    print(solution.maximumRemovals(s = "abcab", p = "abc", removable = [0,1,2,3,4]))