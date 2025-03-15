#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 咒语和药水的成功对数。
时间复杂度：O(Nlogn+N∗Logn)
空间复杂度：O(1)
执行用时：227 ms
消耗内存：37.29 mb
"""
import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = [0] * len(spells)
        for i in range(len(spells)):
            threshold = success / spells[i]
            index = bisect.bisect_left(potions, threshold)
            ans[i] = len(potions) - index
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
    print(s.successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16))
