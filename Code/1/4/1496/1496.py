#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1496.py
作者: Bolun Xu
创建日期: 2025/3/20
版本: 1.0
描述: 判断路径是否相交。
时间复杂度： O(N)
空间复杂度： O(N)
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        location = [[0, 0]]
        for step in path:
            if step == 'N':
                next = [location[-1][0], location[-1][1] + 1]
            elif step == 'S':
                next = [location[-1][0], location[-1][1] - 1]
            elif step == 'E':
                next = [location[-1][0] + 1, location[-1][1]]
            elif step == 'W':
                next = [location[-1][0] - 1, location[-1][1]]
            # print(location, next)
            if next in location:
                return True
            else:
                location.append(next)

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPathCrossing('NESWW'))