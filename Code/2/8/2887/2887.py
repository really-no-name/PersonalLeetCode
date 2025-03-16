#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2887.py
作者: Bolun Xu
创建日期: 2025/3/16
版本: 1.0
描述: 填充缺失值。
时间复杂度：
空间复杂度：
"""
import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products
