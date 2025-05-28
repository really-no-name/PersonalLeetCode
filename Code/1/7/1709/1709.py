#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1709.py
作者: Bolun Xu
创建日期: 2025/5/28
版本: 1.0
描述: 访问日期之间最大的空档期。
"""
import pandas as pd


def biggest_window(user_visits: pd.DataFrame) -> pd.DataFrame:
    data = [['1', '2020-11-28'], ['1', '2020-10-20'], ['1', '2020-12-3'], ['2', '2020-10-5'], ['2', '2020-12-9'],
            ['3', '2020-11-11']]
    user_visits = pd.DataFrame(data, columns=['user_id', 'visit_date']).astype(
        {'user_id': 'Int64', 'visit_date': 'datetime64[ns]'})