#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2885.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 重命名列。
"""
import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    result = students.rename(columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'})
    return result