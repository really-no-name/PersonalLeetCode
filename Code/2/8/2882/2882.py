#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2882.py
作者: Bolun Xu
创建日期: 2025/4/29
版本: 1.0
描述: 删去重复的行。
"""
import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset=['email'], inplace=True)
    return customers

