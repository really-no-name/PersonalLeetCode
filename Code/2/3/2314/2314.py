#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2314.py
作者: Bolun Xu
创建日期: 2025/6/14
版本: 1.0
描述: 每个城市最高气温的第一天。
"""
import pandas as pd


def find_the_first_day(weather: pd.DataFrame) -> pd.DataFrame:
    # 先排序
    df_sort = weather.sort_values(by=['city_id', 'degree', 'day'], ascending=[True, False, True])

    # 去重
    df_drop = df_sort.drop_duplicates(subset=['city_id'], keep='first')
    return df_drop


if __name__ == '__main__':
    data = [[1, '2022-01-07', -12], [1, '2022-03-07', 5], [1, '2022-07-07', 24], [2, '2022-08-07', 37],
            [2, '2022-08-17', 37], [3, '2022-02-07', -7], [3, '2022-12-07', -6]]
    weather = pd.DataFrame(data, columns=['city_id', 'day', 'degree']).astype(
        {'city_id': 'Int64', 'day': 'datetime64[ns]', 'degree': 'Int64'})
    print(find_the_first_day(weather))