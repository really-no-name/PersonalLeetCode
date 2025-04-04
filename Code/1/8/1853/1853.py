#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1853.py
作者: Bolun Xu
创建日期: 2025/4/4
版本: 1.0
描述: 转换日期格式。
"""
import pandas as pd

def format_date(date_str):
    """
    将日期字符串格式化为"day_name, month_name day, year"的格式
    例如: "2022-04-12" -> "Tuesday, April 12, 2022"
    """
    date = pd.to_datetime(date_str)
    return f"{date.day_name()}, {date.month_name()} {date.day}, {date.year}"

def transform_dates(days_df):
    """
    转换Days表中的日期格式
    """
    # 应用format_date函数到每一行
    days_df['day'] = days_df['day'].apply(format_date)
    return days_df

def convert_date_format(days: pd.DataFrame) -> pd.DataFrame:
    result = transform_dates(days)
    return result