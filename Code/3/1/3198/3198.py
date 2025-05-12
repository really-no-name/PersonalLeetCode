#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 3198.py
作者: Bolun Xu
创建日期: 2025/5/12
版本: 1.0
描述: 查找每个州的城市。
"""
import pandas as pd


def find_cities(cities: pd.DataFrame) -> pd.DataFrame:
    df_grp = cities.groupby('state')['city'].agg(lambda x: ', '.join(sorted(x.unique()))).reset_index()
    df_grp = df_grp.rename(columns={'city': 'cities'})
    df_sort = df_grp.sort_values(by=['state'], ascending=True)
    return df_sort


if __name__ == '__main__':
    data = [['California', 'Los Angeles'], ['California', 'San Francisco'], ['California', 'San Diego'],
            ['Texas', 'Houston'], ['Texas', 'Austin'], ['Texas', 'Dallas'], ['New York', 'New York City'],
            ['New York', 'Buffalo'], ['New York', 'Rochester']]
    cities = pd.DataFrame(data, columns=['state', 'city']).astype(str)
    print(find_cities(cities))