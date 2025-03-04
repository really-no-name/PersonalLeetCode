#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1146.py
作者: Bolun Xu
创建日期: 2025/3/4
版本: 1.0
描述: 快照数组。
时间复杂度：
空间复杂度：
"""
from bisect import bisect_left
from collections import defaultdict


class SnapshotArray:

    def __init__(self, length: int):
        """
        初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0
        """
        self.cur_snap_id = 0
        self.history = defaultdict(list)  # 每个 index 的历史修改记录

    def set(self, index: int, val: int) -> None:
        """
        会将指定索引 index 处的元素设置为 val
        """
        self.history[index].append((self.cur_snap_id, val))

    def snap(self) -> int:
        """
        获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）
        :return:
        """
        self.cur_snap_id += 1
        return self.cur_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        """
        根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值
        :param index:
        :param snap_id:
        :return:
        """
        # 找快照编号 <= snap_id 的最后一次修改记录
        # 等价于找快照编号 >= snap_id+1 的第一个修改记录，它的上一个就是答案
        j = bisect_left(self.history[index], (snap_id + 1,)) - 1
        return self.history[index][j][1] if j >= 0 else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)