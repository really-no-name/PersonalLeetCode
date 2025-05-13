#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2883.py
作者: Bolun Xu
创建日期: 2025/5/13
版本: 1.0
描述: 删去丢失的数据。
"""
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    df_filt = students[students['name'].notna()]
    return df_filt