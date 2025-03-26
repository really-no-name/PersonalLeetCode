#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 0611.py
作者: Bolun Xu
创建日期: 2025/3/26
版本: 1.0
描述: 有效三角形的个数。
时间复杂度： O(N^3)
空间复杂度： O(1)
"""
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        ans = 0

        print(f"排序后的数组: {nums}")
        print(f"数组长度: {length}\n")

        for idx_1 in range(length - 2):
            num_1 = nums[idx_1]

            print(f"\n=== 外层循环开始 === idx_1 = {idx_1}, num_1 = {num_1}")

            if num_1 == 0:
                print("跳过，因为第一条边为0不能组成三角形")
                continue

            idx_2 = idx_1 + 1
            print(f"初始化 idx_2 = {idx_2} (nums[{idx_2}] = {nums[idx_2]})")

            for idx_3 in range(idx_1 + 2, length):
                print(f"\n-- 内层循环开始 -- idx_3 = {idx_3}, num_3 = {nums[idx_3]}")
                print(
                    f"当前三角形候选: nums[{idx_1}] = {num_1}, nums[{idx_2}] = {nums[idx_2]}, nums[{idx_3}] = {nums[idx_3]}")

                # 调整idx_2以满足三角形条件
                while idx_2 < idx_3 and nums[idx_3] - nums[idx_2] >= num_1:
                    print(
                        f"不满足条件: nums[{idx_3}]({nums[idx_3]}) - nums[{idx_2}]({nums[idx_2]}) >= nums[{idx_1}]({num_1})")
                    print(f"向右移动idx_2: {idx_2} -> {idx_2 + 1}")
                    idx_2 += 1

                if idx_2 < idx_3:
                    count = idx_3 - idx_2
                    ans += count
                    print(f"找到有效三角形范围: idx_2 = {idx_2}到idx_3-1 = {idx_3 - 1}")
                    print(
                        f"新增 {count} 个三角形: {[f"({num_1},{nums[i]},{nums[idx_3]})" for i in range(idx_2, idx_3)]}")
                    print(f"累计总数更新: {ans - count} -> {ans}")
                else:
                    print(f"idx_2({idx_2}) >= idx_3({idx_3}), 没有有效三角形")

        print("\n=== 最终结果 ===")
        print(f"总有效三角形数量: {ans}")
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.triangleNumber([4, 2, 3, 4]))
