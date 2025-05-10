#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1421.py
作者: Bolun Xu
创建日期: 2025/5/10
版本: 1.0
描述: 净现值查询。
"""
import pandas as pd


def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:
    df_merged = queries.merge(npv, how='left', on=['id', 'year'])
    df_merged['npv'] = df_merged['npv'].fillna(0)
    return df_merged


if __name__ == '__main__':
    data = [[1, 2018, 100],
            [7, 2020, 30],
            [13, 2019, 40],
            [1, 2019, 113],
            [2, 2008, 121],
            [3, 2009, 21],
            [11, 2020, 99],
            [7, 2019, 0]]
    npv = pd.DataFrame(data, columns=['id', 'year', 'npv']).astype({'id': 'Int64', 'year': 'Int64', 'npv': 'Int64'})
    data = [[1, 2019],
            [2, 2008],
            [3, 2009],
            [7, 2018],
            [7, 2019],
            [7, 2020],
            [13, 2019]]
    queries = pd.DataFrame(data, columns=['id', 'year']).astype({'id': 'Int64', 'year': 'Int64'})
    print(npv_queries(npv, queries))
