#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 1294.py
作者: Bolun Xu
创建日期: 2025/5/15
版本: 1.0
描述: 不同国家的天气类型。
"""
import pandas as pd


def weather_type(countries: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    # filter november
    df_filt = weather[(weather['day'] >= '2019-11-01') & (weather['day'] <= '2019-11-30')]
    # calculate mean
    df_grp = df_filt.groupby('country_id')['weather_state'].mean().reset_index()
    df_grp['weather_type'] = df_grp['weather_state'].apply(lambda x: 'Cold' if x <= 15 else ('Hot' if x >= 25 else 'Warm'))
    # merge
    df_merge = df_grp.merge(countries, on='country_id', how='left')
    return df_merge[['country_name', 'weather_type']]


if __name__ == '__main__':
    data = [[2, 'USA'], [3, 'Australia'], [7, 'Peru'], [5, 'China'], [8, 'Morocco'], [9, 'Spain']]
    countries = pd.DataFrame(data, columns=['country_id', 'country_name']).astype(
        {'country_id': 'Int64', 'country_name': 'object'})
    data = [[2, 15, '2019-11-01'], [2, 12, '2019-10-28'], [2, 12, '2019-10-27'], [3, -2, '2019-11-10'],
            [3, 0, '2019-11-11'], [3, 3, '2019-11-12'], [5, 16, '2019-11-07'], [5, 18, '2019-11-09'],
            [5, 21, '2019-11-23'], [7, 25, '2019-11-28'], [7, 22, '2019-12-01'], [7, 20, '2019-12-02'],
            [8, 25, '2019-11-05'], [8, 27, '2019-11-15'], [8, 31, '2019-11-25'], [9, 7, '2019-10-23'],
            [9, 3, '2019-12-23']]
    weather = pd.DataFrame(data, columns=['country_id', 'weather_state', 'day']).astype(
        {'country_id': 'Int64', 'weather_state': 'Int64', 'day': 'datetime64[ns]'})
    print(weather_type(countries, weather))