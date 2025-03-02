#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0904.py
作者: Bolun Xu
创建日期: 2025/3/2
版本: 1.0
描述: 水果成篮。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import defaultdict, Counter
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """

        :param fruits: 树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类
        :return: 可以收集的水果的 最大 数目
        """
        ans = 0
        left = 0
        cnt = Counter()  # or defaultdict(int)
        print(cnt)
        for right, fruit in enumerate(fruits):
            cnt[fruit] += 1

            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    del cnt[fruits[left]]
                left += 1

            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.totalFruit([1, 1, 2]))