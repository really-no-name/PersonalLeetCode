#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2888.py
作者: Bolun Xu
创建日期: 2025/4/28
版本: 1.0
描述: 重塑数据：连结。
"""
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    result = pd.concat([df1, df2], axis=0)
    return result
