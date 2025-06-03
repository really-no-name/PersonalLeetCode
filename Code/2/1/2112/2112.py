#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: PersonalLeetCode 2112.py
作者: Bolun Xu
创建日期: 2025/6/3
版本: 1.0
描述: 最繁忙的机场。
"""
import pandas as pd


def airport_with_most_traffic(flights: pd.DataFrame) -> pd.DataFrame:
    # 分别统计 departure 和 arrival
    df_departure = flights[['departure_airport', 'flights_count']].rename(columns={'departure_airport': 'airport_id', 'flights_count': 'cnt'})
    df_arrival = flights[['arrival_airport', 'flights_count']].rename(columns={'arrival_airport': 'airport_id', 'flights_count': 'cnt'})

    # 合并
    df = pd.concat([df_departure, df_arrival])

    # 求和
    df_grp = df.groupby('airport_id')['cnt'].sum().reset_index()

    # 筛选
    df_filter = df_grp[df_grp['cnt'] == df_grp['cnt'].max()]
    return df_filter[['airport_id']]


if __name__ == '__main__':
    data = [[1, 2, 4], [2, 1, 5], [2, 4, 5]]
    flights = pd.DataFrame(data, columns=['departure_airport', 'arrival_airport', 'flights_count']).astype(
        {'departure_airport': 'Int64', 'arrival_airport': 'Int64', 'flights_count': 'Int64'})
    print('TEST 1\n', airport_with_most_traffic(flights))

    data = [[1, 2, 4],
            [2, 1, 5],
            [3, 4, 5],
            [4, 3, 4],
            [5, 6, 7]]
    flights = pd.DataFrame(data, columns=['departure_airport', 'arrival_airport', 'flights_count']).astype(
        {'departure_airport': 'Int64', 'arrival_airport': 'Int64', 'flights_count': 'Int64'})
    print('TEST 2\n', airport_with_most_traffic(flights))