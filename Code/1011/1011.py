#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 在 D 天内送达包裹的能力。
时间复杂度： O(Nlogn)
空间复杂度： O(N)
执行用时： 255 ms
消耗内存： 21.69 mb
"""
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        # print(f"Debug: Initial bound: {left}, {right}")

        while left < right:
            mid = (left + right) // 2
            # print(f"Debug: 当运载能力为 {mid} 时: ")
            needday = self.needDays(weights, mid)
            # print(f"Debug: 总共需要 {needday} 天")

            if needday > days:
                # print(f"Debug: 大于限定期限，左边界增大")
                left = mid + 1
            else:
                # print(f"Debug: 在限定期限内，右边界减小")
                right = mid
            # print(f"Debug: New bound {left}, {right}")

        return left

    def needDays(self, weights: List[int], ability: int) -> int:
        days = 1
        boat_weight = 0
        boat = []
        for w in weights:
            if boat_weight + w > ability:
                # print(f"Debug:    第 {days} 天，船运 {boat} , 总共重 {boat_weight} ")
                days += 1
                boat_weight = w
                boat = [w]
            else:
                boat_weight += w
                boat.append(w)
        # print(f"Debug:    第 {days} 天，船运 {boat} , 总共重 {boat_weight} ")
        return days


if __name__ == '__main__':
    sol = Solution()
    print("----------------Test 1 ------------------------")
    print(sol.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
    print("----------------Test 2 -----------------------")
    print(sol.shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))
    print("----------------Test 3 -----------------------")
    print(sol.shipWithinDays(weights=[1, 2, 3, 1, 1], days=4))
