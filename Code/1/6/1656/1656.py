#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 设计有序流。
时间复杂度：
空间复杂度：
"""
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 1
        self.list = [""] * (self.n + 1)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey] = value
        start = self.ptr
        while self.ptr < len(self.list) and self.list[self.ptr]:
            self.ptr += 1
        return self.list[start:self.ptr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

if __name__ == '__main__':
    os = OrderedStream(5)
    print(os.insert(3, "ccccc"))  # 插入(3, "ccccc")，返回[]
    print(os.insert(1, "aaaaa"))  # 插入(1, "aaaaa")，返回["aaaaa"]
    print(os.insert(2, "bbbbb"))  # 插入(2, "bbbbb")，返回["bbbbb", "ccccc"]
    print(os.insert(5, "eeeee"))  # 插入(5, "eeeee")，返回[]
    print(os.insert(4, "ddddd"))  # 插入(4, "ddddd")，返回["ddddd", "eeeee"]
