#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 设计内存分配器。
时间复杂度：
空间复杂度：

"""


class Allocator:
    def __init__(self, n: int):
        self.memory = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        free = 0
        for i, id in enumerate(self.memory):
            if id > 0:  # 已分配
                free = 0  # 重新计数
                continue
            free += 1
            if free == size:  # 找到了
                self.memory[i - size + 1: i + 1] = [mID] * size
                return i - size + 1
        return -1  # 无法分配内存

    def freeMemory(self, mID: int) -> int:
        ans = 0
        for i, id in enumerate(self.memory):
            if id == mID:
                ans += 1
                self.memory[i] = 0  # 标记为空闲内存
        return ans


if __name__ == '__main__':
    # Your Allocator object will be instantiated and called as such:
    # obj = Allocator(n)
    # param_1 = obj.allocate(size,mID)
    # param_2 = obj.freeMemory(mID)
    obj = Allocator(n=10)
    param_1 = obj.allocate(size=1, mID=1)
    param_2 = obj.freeMemory(mID)
