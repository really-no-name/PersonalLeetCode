#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1715.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 苹果和橘子的个数。
"""
import pandas as pd


def count_apples_and_oranges(boxes: pd.DataFrame, chests: pd.DataFrame) -> pd.DataFrame:
    data = [[2, None, 6, 15], [18, 14, 4, 15], [19, 3, 8, 4], [12, 2, 19, 20], [20, 6, 12, 9], [8, 6, 9, 9],
            [3, 14, 16, 7]]
    boxes = pd.DataFrame(data, columns=['box_id', 'chest_id', 'apple_count', 'orange_count']).astype(
        {'box_id': 'Int64', 'chest_id': 'Int64', 'apple_count': 'Int64', 'orange_count': 'Int64'})
    data = [[6, 5, 6], [14, 20, 10], [2, 8, 8], [3, 19, 4], [16, 19, 19]]
    chests = pd.DataFrame(data, columns=['chest_id', 'apple_count', 'orange_count']).astype(
        {'chest_id': 'Int64', 'apple_count': 'Int64', 'orange_count': 'Int64'})