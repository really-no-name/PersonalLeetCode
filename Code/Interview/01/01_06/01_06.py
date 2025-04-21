#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 01_06.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 字符串压缩。
时间复杂度： O(N)
空间复杂度： O(N)
"""


class Solution:
    def compressString(self, S: str) -> str:
        if not S: return ""
        result = []
        char = S[0]
        cnt = 0
        for i in range(len(S)):
            if i == len(S) - 1:
                if S[i] != char:
                    result.append(char + str(cnt))
                    char = S[i]
                    cnt = 0
                result.append(char + str(cnt + 1))
            if S[i] != char:
                result.append(char + str(cnt))
                char = S[i]
                cnt = 0
            cnt += 1
        print(result)
        result = ''.join(result)
        if len(result) >= len(S):
            return S
        else:
            return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.compressString("aabcccccaa"))
