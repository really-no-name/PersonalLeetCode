#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1378.py
作者: Bolun Xu
创建日期: 2025/4/21
版本: 1.0
描述: 使用唯一标识码替换员工ID。
"""
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merge_df = pd.merge(employees, employee_uni, on='id', how='left')
    return merge_df[['unique_id', 'name']]