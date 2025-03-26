#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0042.py
作者: Bolun Xu
创建日期: 2025/3/26
版本: 1.0 -- 相向双指针
描述: 接雨水。
时间复杂度： O(N)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        ans = 0

        print(f"初始数组: {height}")
        print(f"初始指针: left={left}(高度{height[left]}), right={right}(高度{height[right]})")
        print(f"初始最大高度: left_max={left_max}, right_max={right_max}\n")

        while left < right:
            print(f"\n--- 当前循环开始 ---")
            print(f"当前指针: left={left}(高度{height[left]}), right={right}(高度{height[right]})")

            # 更新左右最大高度
            left_max_prev = left_max
            right_max_prev = right_max
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            print(f"更新最大高度: left_max {left_max_prev}->{left_max}, right_max {right_max_prev}->{right_max}")

            if height[left] < height[right]:
                added = left_max - height[left]
                ans += added
                print(f"左侧矮: 高度{height[left]} < 高度{height[right]}")
                print(f"  可接雨水: {left_max} - {height[left]} = {added}")
                print(f"  累计雨水: {ans - added} -> {ans}")
                print(f"  左指针移动: {left} -> {left + 1}")
                left += 1
            else:
                added = right_max - height[right]
                ans += added
                print(f"右侧矮: 高度{height[left]} >= 高度{height[right]}")
                print(f"  可接雨水: {right_max} - {height[right]} = {added}")
                print(f"  累计雨水: {ans - added} -> {ans}")
                print(f"  右指针移动: {right} -> {right - 1}")
                right -= 1

            print(f"当前状态: ans={ans}, left={left}, right={right}")

        print("\n--- 循环结束 ---")
        print(f"最终结果: {ans}")
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))