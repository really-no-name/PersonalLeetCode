#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2880.py
作者: Bolun Xu
创建日期: 2025/5/9
版本: 1.0
描述: 数据选取。
"""
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    students_fitered = students[students['student_id'] == 101]
    return students_fitered[['name', 'age']]