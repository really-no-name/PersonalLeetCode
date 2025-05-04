#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2886.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 改变数据类型。
"""
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students = students.astype({'grade': int})
    return students