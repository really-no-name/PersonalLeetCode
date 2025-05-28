#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1699.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 两人之间的通话次数。
"""
import pandas as pd


def number_of_calls(calls: pd.DataFrame) -> pd.DataFrame:
    data = [[1, 2, 59], [2, 1, 11], [1, 3, 20], [3, 4, 100], [3, 4, 200], [3, 4, 200], [4, 3, 499]]
    calls = pd.DataFrame(data, columns=['from_id', 'to_id', 'duration']).astype(
        {'from_id': 'Int64', 'to_id': 'Int64', 'duration': 'Int64'})