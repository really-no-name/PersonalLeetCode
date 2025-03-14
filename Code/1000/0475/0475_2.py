#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0475.py
作者: Bolun Xu
创建日期: 2025/3/5
版本: 2.0
描述: 供暖器。
时间复杂度： O(Nlogn+Mlogm)
空间复杂度： O(1)
"""
import bisect
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
        :param houses:
        :param heaters:
        :return:
        """
        min_r = 0
        heaters.sort()
        for house in houses:
            # 使用 bisect_left 找到插入位置
            right = bisect.bisect_right(heaters, house)
            # left = bisect.bisect_left(heaters, house)
            left = right - 1
            # print(f"DEBUG: 距离 {house} 最近的加热器是 {left} {right}")

            right_distance = heaters[right] - house if right < len(heaters) else float('inf')
            left_distance = house - heaters[left] if left >= 0 else float('inf')
            # print(f"DEBUG: 距离分别是 {left_distance} {right_distance}")

            min_r = max(min_r, min(left_distance, right_distance))

        return min_r


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRadius(houses=[1, 2, 3], heaters=[2]))
    print(sol.findRadius(houses=[1, 2, 3, 4], heaters=[1, 4]))
    print(sol.findRadius(houses=[1, 5], heaters=[2]))
