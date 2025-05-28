#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1613.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 找到遗失的ID。
"""
import pandas as pd


def find_missing_ids(customers: pd.DataFrame) -> pd.DataFrame:
    data = [[1, 'Alice'], [4, 'Bob'], [5, 'Charlie']]
    customers = pd.DataFrame(data, columns=['customer_id', 'customer_name']).astype(
        {'customer_id': 'Int64', 'customer_name': 'object'})