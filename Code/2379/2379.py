#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2379.py
作者: Bolun Xu
创建日期: 2025/2/26
版本: 1.0
描述: 得到 K 个黑块的最少涂色次数。
时间复杂度： O(N)
空间复杂度： O(N)
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        list = []
        for block in blocks:
            list.append(block)
        print(list)

        ans = k
        t = 0
        for i, b in enumerate(list):
            if b == 'W':
                t += 1
            if i < k - 1:
                continue
            ans = min(ans, t)
            if list[i - k + 1] == 'W':
                t -= 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumRecolors(blocks="WBBWWBBWBW", k=7))
