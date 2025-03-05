#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0475.py
作者: Bolun Xu
创建日期: 2025/3/5
版本: 1.0
描述: 供暖器 -- 超出内存限制。
时间复杂度：
空间复杂度：
"""
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
        :param houses:
        :param heaters:
        :return:
        """
        # heaters_location = [0] * len(heaters)
        # for i, heater in enumerate(heaters):
        #     heaters_location[i] = houses.index(heater)
        # print(f"DEBUG: {heaters_location}")

        distances = [[0 for _ in range(len(heaters))] for _ in range(len(houses))]
        house_distance = max(max(houses), max(heaters))
        print(f"DEBUG: {distances}")
        min_r = 0
        for i, house in enumerate(houses):
            print(f"DEBUG:   房子位置为 {house}")
            for j, heater in enumerate(heaters):
                print(f"DEBUG:     加热器位置为 {heater}")
                distances[i][j] = abs(heater - house)
                print(f"DEBUG:     房子 {house} 距加热器 {heater} 的距离为 {abs(heater - house)}")
                house_distance = min(house_distance, distances[i][j])
                print(f"DEBUG:     房子 {house} 距最近的加热器的距离为 {house_distance}")
            print(f"DEBUG: {distances}")
            min_r = max(min_r, house_distance)
            house_distance = max(houses)
        return min_r


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRadius(houses=[1, 2, 3], heaters=[2]))
    print(sol.findRadius(houses=[1, 2, 3, 4], heaters=[1, 4]))
    print(sol.findRadius(houses=[1, 5], heaters=[2]))
