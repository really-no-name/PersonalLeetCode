#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1399.py
作者: Bolun Xu
创建日期: 2025/4/23
版本: 1.0 -- 暴力求解
描述: 统计最大组的数目。
时间复杂度： O(N*M)
空间复杂度： O(N)
"""
from collections import Counter


class Solution:
    def digit_sum(self, n: int) -> int:
        """
        计算数位和
        """
        # 将整数转换为字符串，以便逐个访问每个数字
        num_str = str(n)

        # 初始化总和为0
        total = 0

        # 遍历字符串中的每个字符
        for char in num_str:
            # 将字符转换回整数并加到总和中
            total += int(char)

        # 返回数位和
        return total

    def countLargestGroup(self, n: int) -> int:
        cnt = Counter()
        for i in range(1, n + 1):
            cnt[self.digit_sum(i)] += 1
        print(cnt)
        max_cnt = max(cnt.values())
        ans = 0
        for key in cnt.keys():
            if cnt[key] == max_cnt:
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countLargestGroup(13))