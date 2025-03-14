#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode
作者: Bolun Xu
创建日期: 2025
版本: 1.0
描述: 寻找用户推荐人。
"""
import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer[customer['referee_id'].fillna(0) != 2]
    df = df[['name']]
    return df