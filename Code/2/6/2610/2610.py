#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2610.py
作者: Bolun Xu
创建日期: 2025/3/19
版本: 1.0
描述: 转换二维数组。
时间复杂度： O(N)
空间复杂度： O(N)
"""
from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cnt = Counter(nums)  # 统计每个元素的出现次数
        # print(f"DEBUG: cnt = {cnt}")
        while cnt:  # 还有剩余元素
            row = list(cnt)  # list(cnt)会将cnt中的 键 转换为一个列表
            # print(f"DEBUG: row = {row}")
            ans.append(row)
            # print(f"DEBUG: ans = {ans}")
            # cnt 中的每个元素的出现次数都减一
            for x in row:
                cnt[x] -= 1
                if cnt[x] == 0:
                    del cnt[x]  # 去掉出现次数为 0 的元素
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMatrix([1, 3, 4, 1, 2, 3, 1]))
