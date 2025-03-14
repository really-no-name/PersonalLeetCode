#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 两数之和 III - 数据结构设计。
时间复杂度：
空间复杂度：
执行用时： 261 ms
消耗内存： 22.52 mb
"""


class TwoSum:

    def __init__(self):
        # 使用一个列表来存储所有添加的数字
        self.numbers = []
        # print("Debug: 初始化 TwoSum 对象: numbers = []")

    def add(self, number: int) -> None:
        # 将数字添加到列表中
        self.numbers.append(number)
        # print(f"Debug: 添加数字 {number}: numbers = {self.numbers}")

    def find(self, value: int) -> bool:
        self.numbers.sort()
        left_index = 0
        right_index = len(self.numbers) - 1
        while left_index < right_index:
            s = self.numbers[left_index] + self.numbers[right_index]
            if s == value:
                return True
            elif s < value:
                left_index += 1
            else:
                right_index -= 1
        return False
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


if __name__ == '__main__':
    twoSum = TwoSum()
    twoSum.add(1)
    twoSum.add(3)
    twoSum.add(5)
    twoSum.add(7)
    print(twoSum.find(4))
    print(twoSum.find(7))
