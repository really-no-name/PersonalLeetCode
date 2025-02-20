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
执行用时： 902 ms
消耗内存： 22.67 mb
"""


class TwoSum:

    def __init__(self):
        # 使用一个列表来存储所有添加的数字
        self.numbers = []
        print("Debug: 初始化 TwoSum 对象: numbers = []")

    def add(self, number: int) -> None:
        # 将数字添加到列表中
        self.numbers.append(number)
        print(f"Debug: 添加数字 {number}: numbers = {self.numbers}")

    def find(self, value: int) -> bool:
        # 使用一个集合来存储已经遍历过的数字
        seen = set()
        print(f"Debug: 开始查找两数之和为 {value} 的数字对...")
        for num in self.numbers:
            print(f"Debug: 当前数字: {num}, 需要查找的数字: {value - num}, 已遍历的数字集合: {seen}")
            # 检查是否存在一个数字等于 value - num
            if (value - num) in seen:
                print(f"Debug: 找到数字对: {num} 和 {value - num}, 返回 True")
                return True
            # 将当前数字添加到集合中
            seen.add(num)
            print(f"Debug: 将 {num} 添加到已遍历的数字集合中: {seen}")
        print(f"Debug: 未找到满足条件的数字对, 返回 False")
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
