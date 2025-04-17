#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2418.py
作者: Bolun Xu
创建日期: 2025/4/17
版本: 1.0
描述: 按身高排序。
时间复杂度： O(Nlogn)
空间复杂度： O(N)
"""
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # 将名字和身高组合成元组的列表
        people = list(zip(names, heights))
        # 根据身高降序排序
        people.sort(key=lambda x: x[1], reverse=True)
        # 提取排序后的名字
        result = [person[0] for person in people]
        return result