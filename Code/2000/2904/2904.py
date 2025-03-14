#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2904.py
作者: Bolun Xu
创建日期: 2025/3/14
版本: 1.0
描述: 最短且字典序最小的美丽子字符串 -- 不定长滑窗。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from collections import Counter


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        """
        如果 s 的某个子字符串中 1 的个数恰好等于 k ，则称这个子字符串是一个 美丽子字符串 。
        :param s:
        :param k:
        :param len: 等于 最短 美丽子字符串的长度
        :return:
        """
        if s.count('1') < k:
            return ''

        left = 0
        ans = s
        cnt = 0
        for right, char in enumerate(s):
            # 进入窗口
            cnt += int(char)
            # # 窗口长度不够
            if cnt < k:
                continue
            # 移左
            while cnt > k or s[left] == '0':
                cnt -= int(s[left])
                left += 1
            # 更新答案
            if cnt == k:
                t = s[left: right + 1]
                if len(t) < len(ans) or len(t) == len(ans) and t < ans:
                    ans = t
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.shortestBeautifulSubstring(s = "100011001", k = 3))
