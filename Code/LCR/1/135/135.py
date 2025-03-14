#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 135.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 报数。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def countNumbers(self, cnt: int) -> List[int]:
        ans = []
        i = 1
        while len(str(i)) <= cnt:
            ans.append(i)
            i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countNumbers(1))
    print(s.countNumbers(2))
